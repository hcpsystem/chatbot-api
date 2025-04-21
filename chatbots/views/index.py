from django.http import HttpResponse
# Create your views here.
from rest_framework import viewsets
from rest_framework.decorators import action
from rest_framework.exceptions import APIException, ValidationError
from rest_framework.permissions import AllowAny
from twilio.twiml.messaging_response import MessagingResponse
from core.utils.render import APIRender

from chatbots.services.question import QuestionService
from chatbots.serializers.twilio import TwilioSerializer
from chatbots.services.web import WebService
from chatbots.services.message import MessageService
from chatbots.services.chatbot_responder import ChatbotResponder


class IndexViewSet(viewsets.GenericViewSet):
    @action(detail=False, methods=['GET'], url_path='index')
    def index(self, _):
        return self.show({'app': 'whatsapp'})

    @action(detail=False, methods=['GET'], url_path='questions')
    def question(self, _):
        question = QuestionService()
        question.register()
        return HttpResponse("messages sent!", 200)

    @action(detail=False, methods=['GET'], url_path='welcome')
    def welcome(self, _):
        response = MessagingResponse()
        response.message('¡Hola! Soy Victoria tu asistente virtual de sunafil que te brindara información... !.')
        return HttpResponse(str(response))

    @action(detail=False, methods=['POST'], url_path='message')
    def message(self, request):
        try:
            serializer = TwilioSerializer(data=request.data)
            serializer.is_valid(raise_exception=True)
            data = serializer.validated_data
            return MessageService.response(self, data)

            # handler = MessageService(data)
            # return handler.response()

            # chatbot = ChatbotResponder(data)
            # return chatbot.handle()

            # return MessageService(data).response(self, data)
        except ValidationError as e:
            return APIRender.request_errors(e.detail)
        except APIException as e:
            return APIRender.error(e.detail, e.detail.code)

    @action(detail=False, methods=['GET'], url_path='token', permission_classes=[AllowAny])
    def token(self, request):
        return WebService.token(self, request)
