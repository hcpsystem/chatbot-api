from rest_framework import serializers


class TwilioSerializer(serializers.Serializer):
    _sms_message_sid = serializers.CharField(required=False)
    _num_media = serializers.CharField(required=False)
    _sms_sid = serializers.CharField(required=False)
    _sms_status = serializers.CharField(required=False)
    _body = serializers.CharField(required=False)
    _to = serializers.CharField(required=False)
    _num_segments = serializers.CharField(required=False)
    _message_sid = serializers.CharField(required=False)
    _from = serializers.CharField(required=False)
    _profile_name = serializers.CharField(required=False)
    _wa_id = serializers.CharField(required=False)
    _message_type = serializers.CharField(required=False)
    _referral_num_media = serializers.CharField(required=False)
    _account_sid = serializers.CharField(required=False)
    _api_version = serializers.CharField(required=False)
