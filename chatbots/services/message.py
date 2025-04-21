import os
import json
from datetime import datetime, timedelta, timezone

import pandas as pd
import streamlit as st
from django.http import HttpResponse

from twilio.rest import Client
from twilio.twiml.messaging_response import MessagingResponse

from core.services.app import AppService
from chatbot.models import Answer, Question, Profile
from chatbot.services.send_message import SendMessageService
from core.services.init.accounts.util import InitUtil


class MessageService(AppService):
    def __init__(self, data):
        account_sid = os.environ['TWILIO_ACCOUNT_SID']
        auth_token = os.environ['TWILIO_AUTH_TOKEN']
        self.client = Client(account_sid, auth_token)
        # self.profile_data = {
        #     'name': None,
        #     'from_id': None,
        #     'wa_id': None,
        #     'step': 1,
        #     'is_active': True,
        # }
        self.data = data
        self.limit_minute = int(os.environ['LIMIT_MINUTE_FOR_END'])
        self.date = datetime.now(timezone.utc)
        self.values = []
        self.users = None
        self.question_id = '10'
        self.question_id_old = 0
        self.is_answer = False
        self.is_group = False
        self.is_next_question = True
        self.is_question_old = False
        self.answer_id = 0
        self.category_id = 0
        self.category_name = ''
        self.answer_label = ''
        self.vector = []
        self.rw = []
        self.profile = []

    def get_user_profile(self):
        # Get the user profile or create a new one
        self.load_data_settings()
        to = self.values['_to']
        user = self.values['_from']

        self.users = Profile.objects.filter(to=to, from_id=user).first()
        if self.users:
            self.load_user_settings()
            self.check_inactivity()
        else:
            self.create_new_profile(to, user)

    def load_data_settings(self):
        _sms_message_sid = self.data['_sms_message_sid'] if '_sms_message_sid' in self.data else None
        _num_media = self.data['_num_media'] if '_num_media' in self.data else None
        _sms_sid = self.data['_sms_sid'] if '_sms_sid' in self.data else None
        _sms_status = self.data['_sms_status'] if '_sms_status' in self.data else None
        message = self.data['_body'] if '_body' in self.data else None
        body = self.data['_body'] if '_body' in self.data else None
        to = self.data['_to'] if '_to' in self.data else None
        _num_segments = self.data['_num_segments'] if '_num_segments' in self.data else None
        _message_sid = self.data['_message_sid'] if '_message_sid' in self.data else None
        user = self.data['_from'] if '_from' in self.data else None
        _profile_name = self.data['_profile_name'] if '_profile_name' in self.data else None
        wa_id = self.data['_wa_id'] if '_wa_id' in self.data else None
        _message_type = self.data['_message_type'] if '_message_type' in self.data else None
        _referral_num_media = self.data['_referral_num_media'] if '_referral_num_media' in self.data else None
        _account_sid = self.data['_account_sid'] if '_account_sid' in self.data else None
        _api_version = self.data['_api_version'] if '_api_version' in self.data else None

        self.values = {
            '_sms_message_sid': _sms_message_sid,
            '_num_media': _num_media,
            '_sms_sid': _sms_sid,
            '_sms_status': _sms_status,
            '_body': message,
            '_to': to,
            '_num_segments': _num_segments,
            '_message_sid': _message_sid,
            '_from': user,
            '_profile_name': _profile_name,
            '_wa_id': wa_id,
            '_message_type': _message_type,
            '_referral_num_media': _referral_num_media,
            '_account_sid': _account_sid,
            '_api_version': _api_version
        }

    def load_user_settings(self):
        # Load user settings if available
        home = pd.Series(['go back top', 'Go back top'])
        if self.values['_body'] in home.values:
            self.question_id = '10'
        else:
            if 'question_id' in self.users.settings:
                self.question_id = self.users.settings['question_id']
            if 'question_id_old' in self.users.settings:
                self.question_id_old = self.users.settings['question_id_old']
            if 'is_answer' in self.users.settings:
                self.is_answer = self.users.settings['is_answer']
            if 'answer_id' in self.users.settings:
                self.answer_id = self.users.settings['answer_id']
            if 'category_id' in self.users.settings:
                self.category_id = self.users.settings['category_id']
            if 'category_name' in self.users.settings:
                self.category_name = self.users.settings['category_name']
            if 'vectorial' in self.users.settings:
                self.vector = self.users.settings['vectorial']
            if 'answer_label' in self.users.settings:
                self.answer_label = self.users.settings['answer_label']

    def check_inactivity(self):
        # Check if the user has been inactive for too long
        if self.users.updated_at:
            last_activity = self.users.updated_at + timedelta(minutes=self.limit_minute)
            if self.date > last_activity:
                self.reset_user_flow()

    def reset_user_flow(self):
        # Reset user question flow if inactive
        self.question_id = '13'
        self.is_answer = False

    def create_new_profile(self, to, user):
        # Create a new profile if the user doesn't exist
        total = Profile.objects.all().count()
        id = total + 1
        Profile.objects.create(
            id=id,
            to=to,
            from_id=user,
            name=self.values['_body'],
            wa_id=self.values['_wa_id'],
            settings={
                'question_id': self.question_id,
                'answer_id': self.answer_id,
                'is_answer': False,
            }
        )

    def process_message(self):
        # Process the incoming message to determine the next question/response
        try:
            number = int(self.values['_body'])
        except (ValueError, TypeError):
            number = 0

        response = MessagingResponse()
        if self.is_answer:
            response = self.process_answer(number, response)
        else:
            question = Question.objects.filter(flow_id=self.question_id).first()
            self.is_group = question.settings['is_group'] if 'is_group' in question.settings else False
        return self.process_question_flow(number, response)

    def process_answer(self, number, response):
        # Process the answer if the user has responded to a question
        question_valid = self.question_id_old

        if question_valid == '12.1':
            self.question_id = '13'
            self.question_id_old = '13'
            self.is_next_question = True
            self.is_question_old = True
            if number < 18:
                response.message('🚨 ¡RECUERDA! \n Se encuentra prohibido el trabajo del hogar para menores de edad')
        elif question_valid == '14.2.2.1.1.1':
            return response
        else:
            self.question_id_old = str(self.question_id_old) + '.' + str(number)
            answer = Question.objects.filter(flow_id=self.question_id_old).first()
            if not answer or number == 0:
                response.message(
                    f'Lo siento, no tenemos la opción {self.values["_body"]} ¿Puedes volver a digitar la alternativa?.')
            else:
                self.handle_answer_flow(answer, response)
        return response

    def handle_answer_flow(self, answer, response):
        settings = answer.settings.get('questions', [])
        self.is_group = answer.settings.get('is_group', False)

        for s in settings:
            self.question_id = s

    def process_question_flow(self, number, response):
        # Process the flow of questions
        question_all = [self.question_id]
        rw = []

        while self.is_next_question:
            self.is_next_question = False
            for question_id in question_all:
                self.question_id_old = question_id if not self.is_question_old else self.question_id_old

                questions = Question.objects.filter(parent_id=question_id).order_by('id')
                self.is_question_old = False
                if questions:
                    for question in questions:
                        self.handle_question(question, rw, response)
                    next_question = question.settings.get('is_reload', False)
                if self.is_next_question:
                    question_all = question.settings.get('questions', [])
        return response

    def handle_question(self, question, rw, response):
        is_group = question.settings.get('is_group', False)
        if is_group:
            rw.append(f'{question.name} \n')
        else:
            response.message(f'{question.name} \n')

    def update_profile(self):
        # Update the profile with the current settings
        defaults = {
            'updated_at': self.date,
            'settings': {
                "question_id": self.question_id,
                "question_id_old": self.question_id_old,
                "is_answer": self.is_answer,
                "message": self.data['_body'],
            },
        }
        to = self.data['_to'] if '_to' in self.data else None
        user = self.data['_from'] if '_from' in self.data else None
        Profile.objects.filter(to=to, from_id=user).update(**defaults)

    def generate_response(self, response):
        # Generate the final response
        # response = MessagingResponse()
        if self.is_group:
            if self.rw:
                response.message(''.join(map(str, self.rw)))
        return HttpResponse(str(response))

    def response_old(self):
        # Main handler function to process everything
        self.get_user_profile()
        response = self.process_message()
        self.update_profile()
        return self.generate_response(response)

    def response(self, data):
        # Whatsapp
        # try:
        limit_minute = os.environ['LIMIT_MINUTE_FOR_END']

        _sms_message_sid = data['_sms_message_sid'] if '_sms_message_sid' in data else None
        _num_media = data['_num_media'] if '_num_media' in data else None
        _sms_sid = data['_sms_sid'] if '_sms_sid' in data else None
        _sms_status = data['_sms_status'] if '_sms_status' in data else None
        message = data['_body'] if '_body' in data else None
        body = data['_body'] if '_body' in data else None
        to = data['_to'] if '_to' in data else None
        _num_segments = data['_num_segments'] if '_num_segments' in data else None
        _message_sid = data['_message_sid'] if '_message_sid' in data else None
        user = data['_from'] if '_from' in data else None
        _profile_name = data['_profile_name'] if '_profile_name' in data else None
        wa_id = data['_wa_id'] if '_wa_id' in data else None
        _message_type = data['_message_type'] if '_message_type' in data else None
        _referral_num_media = data['_referral_num_media'] if '_referral_num_media' in data else None
        _account_sid = data['_account_sid'] if '_account_sid' in data else None
        _api_version = data['_api_version'] if '_api_version' in data else None

        users = Profile.objects.filter(to=to, from_id=user).first()
        question_id = '10'
        question_id_old = 0
        is_answer = False
        is_group = False
        answer_id = 0
        category_id = 0
        category_name = ''
        answer_label = ''
        date = datetime.now(timezone.utc)
        vector = []
        is_reload = False
        # Register User and Password

        # InitUtil.find_user()

        if users:
            # Inicio
            home = pd.Series(['go back top', 'Go back top', 'dppr borrar sesion', 'Dppr borrar sesion'])

            if message in home.values:
                defaults = {
                    'updated_at': date,
                    'from_id': user + '_old',
                }
                is_reload = True
                Profile.objects.filter(to=to, from_id=user).update(**defaults)

            if 'question_id' in users.settings:
                question_id = question_id if message in home.values else users.settings['question_id']
            if 'question_id_old' in users.settings:
                question_id_old = question_id_old if message in home.values else users.settings['question_id_old']
            if 'is_answer' in users.settings:
                is_answer = is_answer if message in home.values else users.settings['is_answer']
            if 'answer_id' in users.settings:
                answer_id = answer_id if message in home.values else users.settings['answer_id']
            if 'category_id' in users.settings:
                category_id = category_id if message in home.values else users.settings['category_id']
            if 'category_name' in users.settings:
                category_name = category_name if message in home.values else users.settings['category_name']
            if 'vectorial' in users.settings:
                vector = vector if message in home.values else users.settings['vectorial']
            if 'answer_label' in users.settings:
                answer_label = answer_label if message in home.values else users.settings['answer_label']

            if users.updated_at:
                print(users.updated_at + timedelta(minutes=int(limit_minute)))
                date_old = users.updated_at + timedelta(minutes=int(limit_minute))
                print('date_old')
                print(date_old)
                if date > date_old:
                    # question_id = '10' if question_id > '7' else question_id
                    # is_answer = False if question_id > '7' else question_id
                    question_id = '13'
                    is_answer = False

        else:
            total = Profile.objects.all().count()
            id = total + 1
            Profile.objects.create(
                **{
                    'id': id,
                    'to': to,
                    'from_id': user,
                    'name': body,
                    'wa_id': wa_id,
                    'settings': {'question_id': question_id, 'answer_id': answer_id, 'is_answer': False},
                }
            )

        try:
            number = int(message)
        except (ValueError, TypeError):
            number = 0

        response = MessagingResponse()
        rw = []
        if is_reload:
            is_group = True
            rw.append('El chatbot se ha reiniciado. Ahora puede comenzar de nuevo. \n')
            # response.message('El chatbot se ha reiniciado. Ahora puede comenzar de nuevo.')

        else:
            next = True
            is_question_old = False
            print(':::::is_answer:::::')
            if is_answer:
                question_valid = question_id_old
                print('question_id_old')
                print(question_id_old)
                if question_valid == '12.1':
                    question_id = '13'
                    question_id_old = '13'
                    is_question_old = True
                    next = True
                    if number < 18:
                        response.message('🚨 ¡RECUERDA! \n Se encuentra prohibido el trabajo del '
                                         'hogar para menores de edad')

                elif question_valid == '14.2.2.1.1.1':
                    next = False

                else:
                    question_id_old = str(question_id_old) + '.' + str(number)
                    answer = Question.objects.filter(flow_id=question_id_old).first()
                    if not answer or number == 0:
                        next = False
                        response.message(f'Lo siento, no tenemos la opción {message} ¿Puedes volver a digitar la '
                                         f'alternativa?.')
                    else:
                        settings = answer.settings['questions'] if 'questions' in answer.settings else None
                        is_group = answer.settings['is_group'] if 'is_group' in answer.settings else False
                        settings_next = answer.settings['questions_next'] if 'questions_next' in answer.settings else None
                        print('settings_next')
                        print(settings_next)
                        print(is_group)
                        print(settings)
                        if settings_next:
                            for s in settings_next:
                                question_id = s
                        else:
                            if settings:
                                for s in settings:
                                    question_id = s
            else:
                print(':::::Else:::::')
                print(question_id)
                question = Question.objects.filter(flow_id=question_id).first()
                is_group = question.settings['is_group'] if 'is_group' in question.settings else False
                settings = question.settings['questions_next'] if 'questions_next' in question.settings else None
                if settings:
                    for s in settings:
                        question_id = s
                if question_id == question_id_old and question_id_old == '14.2':
                    question_id = '14.2.2'

            if (question_id == question_id_old and question_id_old == '14.3' and not is_answer) or \
                    (question_id == question_id_old and question_id_old == '14.2.2'):
                response.message(f'¡Hola! Un gusto volver a verte 🤗')
                question_id = '13'

            print(':::::question_all:::::')
            question_all = [question_id]

            while next:
                next = False
                print('Start')
                print(question_all)
                for question_id in question_all:
                    if not is_question_old:
                        question_id_old = question_id
                    questions = Question.objects.filter(parent_id=question_id).order_by('id')
                    settings = None
                    is_reload = False
                    is_question_old = False
                    if questions:
                        r = []
                        isGChld = False
                        for question in questions:
                            isGChld = question.settings['is_group'] if 'is_group' in question.settings else None
                            is_reload = question.settings['is_reload'] if 'is_reload' in question.settings else False
                            if is_reload:
                                settings_reload = question.settings['questions'] if 'questions' in question.settings \
                                    else False

                            if isGChld or is_group:
                                print('::isGChld')
                                print(isGChld)
                                if question.is_read:
                                    r.append(f'{question.name.replace("XXXXXX", message)} \n ')
                                    rw.append(f'{question.name.replace("XXXXXX", message)} \n ')
                                else:
                                    r.append(f'{question.name} \n ')
                                    rw.append(f'{question.name} \n ')
                            else:
                                print('::not isGChld')
                                if question.is_read:
                                    response.message(f'{question.name.replace("XXXXXX", message)}')
                                else:
                                    response.message(f'{question.name} \n ')

                        if not is_group:
                            print('is_group :: 1')
                            print(is_group)
                            if isGChld:
                                if len(r) > 0:
                                    lol_string = ''.join(map(str, r))
                                    response.message(f'{lol_string}')

                    print(':::=>question_id::::')
                    print(question_id)
                    next = is_reload
                    question = Question.objects.filter(flow_id=question_id).first()
                    settings = question.settings['questions'] if 'questions' in question.settings else None
                    is_answer = question.settings['is_answer'] if 'is_answer' in question.settings else None
                    if settings:
                        for s in settings:
                            question_id = s

                    # "answer_id": answer_id,
                    # "category_id": category_id,
                    # "category_name": category_name,
                    # "answer_label": answer_label,
                    defaults = {
                        'updated_at': date,
                        'settings': {
                            "question_id": question_id,
                            "question_id_old": question_id_old,
                            "is_answer": is_answer,
                            "message": message,
                        },
                    }
                    Profile.objects.filter(to=to, from_id=user).update(**defaults)
                    if is_reload:
                        if settings_reload:
                            question_all = settings_reload
                            print('::settings:: For')
                            print(question_all)
                    if is_group:
                        if len(rw) > 0:
                            rw.append('\n')
            if is_group:
                print('is_group :: 2')
                print(is_group)
                print(rw)
                if len(rw) > 0:
                    lol_string = ''.join(map(str, rw))
                    response.message(f'{lol_string}')

        return HttpResponse(str(response))

        # except:
        #     response = MessagingResponse()
        #     response.message('Error Respuesta incorecta !')
        # return HttpResponse(str(response))

    def load_data_profile(data):
        return {
            'first_name': data['first_name'],
            'last_name': data['last_name'],
            'country_code': data['country_code'],
            'phone': data['phone'],
            'step': 'home',
            'is_active': data['is_active'],
            'email': data['email'],
            'username': data['username'],
            'email_verified_at': data['email_verified_at'],
            'image_pin': data['image_pin'],
            'photo': data['photo'],
            'status': USER_STATUS.COMPLETED,
            'role': USER_ROLES.ACCOUNT,
            'position': data['position'],
        }

    def create(self, data):
        # Whatsapp
        # try:
        limit_minute = os.environ['LIMIT_MINUTE_FOR_END']

        _sms_message_sid = data['_sms_message_sid'] if '_sms_message_sid' in data else None
        _num_media = data['_num_media'] if '_num_media' in data else None
        _sms_sid = data['_sms_sid'] if '_sms_sid' in data else None
        _sms_status = data['_sms_status'] if '_sms_status' in data else None
        message = data['_body'] if '_body' in data else None
        body = data['_body'] if '_body' in data else None
        to = data['_to'] if '_to' in data else None
        _num_segments = data['_num_segments'] if '_num_segments' in data else None
        _message_sid = data['_message_sid'] if '_message_sid' in data else None
        user = data['_from'] if '_from' in data else None
        _profile_name = data['_profile_name'] if '_profile_name' in data else None
        wa_id = data['_wa_id'] if '_wa_id' in data else None
        _message_type = data['_message_type'] if '_message_type' in data else None
        _referral_num_media = data['_referral_num_media'] if '_referral_num_media' in data else None
        _account_sid = data['_account_sid'] if '_account_sid' in data else None
        _api_version = data['_api_version'] if '_api_version' in data else None

        users = Profile.objects.filter(to=to, from_id=user).first()
        question_id = 1
        question_id_old = 0
        is_answer = False
        answer_id = 0
        category_id = 0
        category_name = ''
        answer_label = ''
        date = datetime.now(timezone.utc)
        vector = []

        if users:
            # Inicio
            home = pd.Series(['go back top', 'Go back top'])

            if 'question_id' in users.settings:
                question_id = question_id if message in home.values else users.settings['question_id']
            if 'question_id_old' in users.settings:
                question_id_old = question_id_old if message in home.values else users.settings['question_id_old']
            if 'is_answer' in users.settings:
                is_answer = is_answer if message in home.values else users.settings['is_answer']
            if 'answer_id' in users.settings:
                answer_id = answer_id if message in home.values else users.settings['answer_id']
            if 'category_id' in users.settings:
                category_id = category_id if message in home.values else users.settings['category_id']
            if 'category_name' in users.settings:
                category_name = category_name if message in home.values else users.settings['category_name']
            if 'vectorial' in users.settings:
                vector = vector if message in home.values else users.settings['vectorial']
            if 'answer_label' in users.settings:
                answer_label = answer_label if message in home.values else users.settings['answer_label']

            if users.updated_at:
                print('date')
                print(date)
                print('updated_at')
                print(users.updated_at)
                print('timedelta')
                print(users.updated_at + timedelta(minutes=int(limit_minute)))
                date_old = users.updated_at + timedelta(minutes=int(limit_minute))
                print('date_old')
                print(date_old)
                if date > date_old:
                    question_id = 10 if question_id > 7 else question_id
                    is_answer = False if question_id > 7 else question_id

        else:
            total = Profile.objects.all().count()
            id = total + 1
            Profile.objects.create(
                **{
                    'id': id,
                    'to': to,
                    'from_id': user,
                    'name': body,
                    'wa_id': wa_id,
                    'settings': {'question_id': question_id, 'answer_id': answer_id, 'is_answer': False},
                }
            )

        try:
            number = int(message)
        except (ValueError, TypeError):
            number = 0

        response = MessagingResponse()
        next = True
        match question_id:
            case 20:
                query = message
                if 'responses' not in st.session_state:
                    st.session_state['responses'] = ["¿Como puedo ayudarte?"]

            case 1 | 2 | 3 | 4 | 6 | 7 | 9 | 10 | 11 | 12 | 13:
                print('Question::1')
                print(question_id)
                print(question_id_old)
                question_all = [question_id]

                if is_answer:
                    answer = Answer.objects.filter(question=question_id_old, order=number).first()
                    if not answer:
                        next = False
                        response.message(f'Lo siento, no tenemos la opción {message} ¿Puedes volver a digitar la '
                                         f'alternativa?.')
                    else:
                        settings = answer.settings['questions'] if 'questions' in answer.settings else None
                        if settings:
                            question_all = settings
                        answer_id = answer.order
                        if question_id_old == 3:
                            category_id = answer.order
                            category_name = answer.label
                        if question_id_old == 8:
                            answer_label = answer.label
            case 5:
                next = True
                # if is_answer:
                if 0 < number < 18:
                    question_all = [6]
                elif number > 100:
                    next = False
                    response.message(f'Respuesta incorecta !.{message}')
                else:
                    question_all = [7, 8]
            case 8:
                question_all = [7, 8]

            case 15:
                is_msg = True
                if is_answer:
                    for vt in vector:
                        if vt['id'] == number:
                            is_msg = vt['is_valid']
                            if vt['is_valid']:
                                message = vt['name']
                            else:
                                next = False
                                response.message('Puedes escribir otra consulta. ✍️\n')

            case _:  # change this in default
                response.message(f'Respuesta incorecta !.{message}')

        if next:
            for question_id in question_all:
                question_id_old = question_id
                r = []
                question = Question.objects.filter(flow_id=question_id).first()
                if question:
                    is_answer = question.is_options
                    content_sid = None
                    print(user)
                    if 'whatsapp' in user:
                        print('whatsapp')
                        content_sid = question.content_sid
                    if content_sid:
                        SendMessageService.send_content(content_sid, user, message)
                    else:
                        if question.is_read:
                            # print('is_read')
                            # hola = question.name
                            # question_name = hola.replace('XXXXXX', message)
                            # print(question_name)
                            response.message(f'{question.name.replace("XXXXXX", message)}')
                            # response.message(f'{question_name.replace("XXXXXX", message)}')
                            # response.message(f'{question_name}')
                            # SendMessageService.send_message(to, user, f'{question.name.replace("XXXXXX", message)}')
                            # response.message(f'{message}')
                        answer = Answer.objects.filter(question=question.id).order_by('order')
                        if answer:
                            for asw in answer:
                                if asw.id == 2:
                                    # response.body("imagen")
                                    response.message().media(
                                        "https://victoriasunafil.net.pe/static/trabajo_domestico.png")
                                else:
                                    if question.is_options:
                                        r.append(f'{asw.order}. {asw.name} \n ')
                                    else:
                                        response.message(f'{asw.name} \n ')
                        if question.is_options:
                            lol_string = ''.join(map(str, r))
                            response.message(f'{lol_string}')
                            # response.message({
                            #     "give you up",
                            #     "let you down",
                            #     "run around and desert you",
                            #     "make you cry",
                            #     "say goodbye",
                            #     "tell a lie, and hurt you"
                            # })
                            # response.message("Option 1").list_picker("option1")
                            # response.message("Option 2").list_picker("option2")
                            # response.message("Option 3").list_picker("option3")

                    settings = question.settings['questions'] if 'questions' in question.settings else None

                    if settings:
                        for s in settings:
                            question_id = s

                    defaults = {
                        'updated_at': date,
                        'settings': {
                            "question_id": question_id,
                            "answer_id": answer_id,
                            "question_id_old": question_id_old,
                            "is_answer": is_answer,
                            "category_id": category_id,
                            "category_name": category_name,
                            "answer_label": answer_label,
                            "message": message,
                        },
                    }
                    Profile.objects.filter(to=to, from_id=user).update(**defaults)
        else:
            defaults = {
                'updated_at': date,
                'settings': {
                    "question_id": question_id,
                    "answer_id": answer_id,
                    "question_id_old": question_id_old,
                    "is_answer": is_answer,
                    "category_id": category_id,
                    "category_name": category_name,
                    "answer_label": answer_label,
                    "vectorial": vector,
                    "message": message,
                },
            }
            Profile.objects.filter(to=to, from_id=user).update(**defaults)

        return HttpResponse(str(response))

        # except:
        #     response = MessagingResponse()
        #     response.message('Error Respuesta incorecta !')
        #     return HttpResponse(str(response))

    def send_message(self, to, of, body):
        # account_sid = os.environ['TWILIO_ACCOUNT_SID']
        # auth_token = os.environ['TWILIO_AUTH_TOKEN']
        # client = Client(account_sid, auth_token)
        messaging_service_sid = os.environ['TWILIO_MESSAGING_SERVICE_SID']
        return self.client.messages.create(to=to, messaging_service_sid=messaging_service_sid, body=body, from_=of)

    def replace_label(self):
        pass
