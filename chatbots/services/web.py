import os
import uuid

from django.http import JsonResponse
from twilio.jwt.access_token import AccessToken
from twilio.jwt.access_token.grants import ChatGrant
from chatbots.serializers.web import WebLoginValidatorSerializer


class WebService:
    def token(self, request):
        serializer = WebLoginValidatorSerializer(data=request.query_params)
        serializer.is_valid(raise_exception=True)

        account_sid = os.environ['TWILIO_ACCOUNT_SID']
        api_key = os.environ['TWILIO_API_KEY']
        api_secret = os.environ['TWILIO_API_KEY_SECRET']

        service_sid = os.environ['TWILIO_SERVICE_SID']
        # identity = 'user@example.com'
        # service_sid = service.sid
        identity = f"{serializer.validated_data['name']}{str(uuid.uuid4())}"
        # identity = 'Vitoria'

        # Create access token with credentials
        token = AccessToken(account_sid, api_key, api_secret, identity=identity)

        # Create an Chat grant and add to token
        chat_grant = ChatGrant(service_sid=service_sid)
        token.add_grant(chat_grant)

        # Return token info as JSON
        jwt = token.to_jwt()
        # return HttpResponse(str(jwt))
        return JsonResponse({'identity': identity, 'jwt': jwt, 'token': jwt})
