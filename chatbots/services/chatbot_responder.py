import os
import logging
from datetime import datetime, timezone, timedelta
import pandas as pd
from django.http import HttpResponse
from twilio.twiml.messaging_response import MessagingResponse
from chatbot.models import Profile, Question, Response

logger = logging.getLogger(__name__)


class ChatbotResponder:
    def __init__(self, data):
        self.data = data
        self.response = MessagingResponse()
        self.date = datetime.now(timezone.utc)
        self.limit_minute = int(os.environ.get('LIMIT_MINUTE_FOR_END', 30))

        # Variables iniciales
        self.message = self.get('_body')
        self.user = self.get('_from')
        self.to = self.get('_to')
        self.body = self.message
        self.wa_id = self.get('_wa_id')

        self.question_id = '10'
        self.question_id_old = 0
        self.is_answer = False
        self.is_group = False
        self.answer_id = 0
        self.category_id = 0
        self.category_name = ''
        self.answer_label = ''
        self.vector = []
        self.is_reload = False
        self.rw = []

        self.home = pd.Series(['go back top', 'Go back top', 'dppr borrar sesion', 'Dppr borrar sesion'])

    def get(self, key, default=None):
        return self.data.get(key, default)

    def update_profile_settings(self, updates):
        Profile.objects.filter(to=self.to, from_id=self.user).update(**updates)

    def get_or_create_profile(self):
        profile = Profile.objects.filter(to=self.to, from_id=self.user).first()
        if profile:
            return profile

        new_id = Profile.objects.all().count() + 1
        profile = Profile.objects.create(
            id=new_id,
            to=self.to,
            from_id=self.user,
            name=self.body,
            wa_id=self.wa_id,
            settings={'question_id': self.question_id, 'answer_id': self.answer_id, 'is_answer': False}
        )
        return profile

    def restore_user_settings(self, profile):
        s = profile.settings
        if self.message in self.home.values:
            self.is_reload = True
            self.update_profile_settings({
                'updated_at': self.date,
                'from_id': self.user + '_old',
            })

        self.question_id = self.question_id if self.message in self.home.values else s.get('question_id',
                                                                                           self.question_id)
        self.question_id_old = self.question_id_old if self.message in self.home.values else s.get(
            'question_id_old', self.question_id_old)
        self.is_answer = self.is_answer if self.message in self.home.values else s.get('is_answer', self.is_answer)
        self.answer_id = s.get('answer_id', self.answer_id)
        self.category_id = s.get('category_id', self.category_id)
        self.category_name = s.get('category_name', self.category_name)
        self.vector = s.get('vectorial', self.vector)
        self.answer_label = s.get('answer_label', self.answer_label)

        if profile.updated_at and self.date > profile.updated_at + timedelta(minutes=self.limit_minute):
            self.question_id = '13'
            self.is_answer = False

    def handle(self):
        try:
            self.number = int(self.message)
        except (ValueError, TypeError):
            self.number = 0

        profile = self.get_or_create_profile()
        #
        self.save_user_response(profile)
        #
        self.restore_user_settings(profile)

        if self.is_reload:
            self.is_group = True
            self.rw.append('El chatbot se ha reiniciado. Ahora puede comenzar de nuevo. \n')
        else:
            self.process_questions(profile)

        if self.is_group and self.rw:
            self.response.message(''.join(self.rw))

        return HttpResponse(str(self.response))

    def process_questions(self, profile):
        next_step = True
        is_question_old = False

        if self.is_answer:
            if self.question_id_old == '12.1':
                if self.number < 18:
                    self.response.message(
                        '🚨 ¡RECUERDA! \n Se encuentra prohibido el trabajo del hogar para menores de edad')
                self.question_id = self.question_id_old = '13'
                is_question_old = True

            elif self.question_id_old == '14.2.2.1.1.1':
                next_step = False

            else:
                self.question_id_old = f'{self.question_id_old}.{self.number}'
                answer = Question.objects.filter(flow_id=self.question_id_old).first()
                if not answer or self.number == 0:
                    next_step = False
                    self.response.message(
                        f'Lo siento, no tenemos la opción {self.message}. ¿Puedes volver a digitar la alternativa?')
                else:
                    self.is_group = answer.settings.get('is_group', False)
                    next_qs = answer.settings.get('questions_next')
                    alt_qs = answer.settings.get('questions')
                    if next_qs:
                        self.question_id = next_qs[0]
                    elif alt_qs:
                        self.question_id = alt_qs[0]
        else:
            current = Question.objects.filter(flow_id=self.question_id).first()
            if current:
                self.is_group = current.settings.get('is_group', False)
                next_qs = current.settings.get('questions_next')
                if next_qs:
                    self.question_id = next_qs[0]

            if self.question_id == self.question_id_old == '14.2':
                self.question_id = '14.2.2'

        if self.question_id == self.question_id_old and self.question_id in ['14.3',
                                                                             '14.2.2'] and not self.is_answer:
            self.response.message('¡Hola! Un gusto volver a verte 🤗')
            self.question_id = '13'

        self.show_question_flow(profile, [self.question_id], is_question_old)

    def show_question_flow(self, profile, question_list, is_question_old):
        next_step = True
        while next_step:
            next_step = False
            for qid in question_list:
                if not is_question_old:
                    self.question_id_old = qid

                questions = Question.objects.filter(parent_id=qid).order_by('id')
                if questions:
                    group_block = []
                    for q in questions:
                        content = q.name.replace('XXXXXX', self.message) if q.is_read else q.name
                        if q.settings.get('is_group', False) or self.is_group:
                            group_block.append(f'{content} \n ')
                            self.rw.append(f'{content} \n ')
                        else:
                            self.response.message(content)

                        if q.settings.get('is_reload', False):
                            next_step = True
                            question_list = q.settings.get('questions', [])

                    if not self.is_group and group_block:
                        self.response.message(''.join(group_block))

                main_question = Question.objects.filter(flow_id=qid).first()
                if main_question:
                    self.is_answer = main_question.settings.get('is_answer', False)
                    next_qs = main_question.settings.get('questions')
                    if next_qs:
                        self.question_id = next_qs[0]

                self.update_profile_settings({
                    'updated_at': self.date,
                    'settings': {
                        "question_id": self.question_id,
                        "question_id_old": self.question_id_old,
                        "is_answer": self.is_answer,
                        "message": self.message,
                    }
                })

    def save_user_response(self, profile):
        current_question = Question.objects.filter(flow_id=self.question_id).first()
        question_text = current_question.name if current_question else None

        try:
            selected_option = int(self.message)
        except (ValueError, TypeError):
            selected_option = None

        Response.objects.create(
            profile=profile,
            question_id=self.question_id,
            question_text=question_text,
            selected_option=selected_option,
            message=self.message,
            is_bot=False
        )
