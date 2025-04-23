import os
from datetime import datetime, timedelta, timezone

import pandas as pd
from django.http import HttpResponse

from twilio.twiml.messaging_response import MessagingResponse

from core.services.app import AppService
from chatbots.models import Question
from users.models import User


class MessageService(AppService):
    def response(self, data):
        # Whatsapp
        try:
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

            users = User.objects.filter(to=to, from_id=user).first()
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
                    User.objects.filter(to=to, from_id=user).update(**defaults)

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
                    date_old = users.updated_at + timedelta(minutes=int(limit_minute))
                    if date > date_old:
                        # question_id = '10' if question_id > '7' else question_id
                        # is_answer = False if question_id > '7' else question_id
                        question_id = '13'
                        is_answer = False

            else:
                total = User.objects.all().count()
                id = total + 1
                User.objects.create(
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
                if is_answer:
                    question_valid = question_id_old
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
                            settings_next = answer.settings[
                                'questions_next'] if 'questions_next' in answer.settings else None
                            if settings_next:
                                for s in settings_next:
                                    question_id = s
                            else:
                                if settings:
                                    for s in settings:
                                        question_id = s
                else:
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

                question_all = [question_id]

                while next:
                    next = False
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
                                is_reload = question.settings[
                                    'is_reload'] if 'is_reload' in question.settings else False
                                if is_reload:
                                    settings_reload = question.settings['questions'] if 'questions' in question.settings \
                                        else False

                                if isGChld or is_group:
                                    if question.is_read:
                                        r.append(f'{question.name.replace("XXXXXX", message)} \n ')
                                        rw.append(f'{question.name.replace("XXXXXX", message)} \n ')
                                    else:
                                        r.append(f'{question.name} \n ')
                                        rw.append(f'{question.name} \n ')
                                else:
                                    if question.is_read:
                                        response.message(f'{question.name.replace("XXXXXX", message)}')
                                    else:
                                        response.message(f'{question.name} \n ')

                            if not is_group:
                                if isGChld:
                                    if len(r) > 0:
                                        lol_string = ''.join(map(str, r))
                                        response.message(f'{lol_string}')

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
                        User.objects.filter(to=to, from_id=user).update(**defaults)
                        if is_reload:
                            if settings_reload:
                                question_all = settings_reload
                        if is_group:
                            if len(rw) > 0:
                                rw.append('\n')
                if is_group:
                    if len(rw) > 0:
                        lol_string = ''.join(map(str, rw))
                        response.message(f'{lol_string}')

            return HttpResponse(str(response))

        except:
            response = MessagingResponse()
            response.message('Error chatbot incorecta !')
            return HttpResponse(str(response))
