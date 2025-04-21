import hashlib
import json
import random
import re
from datetime import datetime, timedelta, timezone
from functools import reduce

from django.conf import settings
from django.core import serializers
from django.core.mail import EmailMultiAlternatives, send_mail
from django.http import HttpResponsePermanentRedirect
from django.template.loader import render_to_string


class SchemeRedirectUtil(HttpResponsePermanentRedirect):
    """
    An HttpResponse that allows redirect to a specific scheme
    """

    allowed_schemes = ['chatbot']


class AppUtil:
    @staticmethod
    def send_email(subject, message, to_emails):
        send_mail(
            subject,
            message,
            settings.EMAIL_FROM_ADDRESS,
            to_emails,
            fail_silently=False,
        )

    @staticmethod
    def send_html_email(to, subject, template, context=''):
        """
        Send email function

        :param to: (email) recipient
        :param subject: (string) mail subject
        :param template: (string) mail template
        :param context: (dict) email data
        """
        if context:
            html_content = render_to_string(template, context)
            email = EmailMultiAlternatives(
                subject=subject,
                body=subject,
                from_email=settings.EMAIL_FROM_ADDRESS,
                to=[to],
            )
            email.attach_alternative(html_content, 'text/html')
            email.send()

    @staticmethod
    def generate_random_number(length):
        """
        Function to generate random number

        :param length: Number length
        :return number: Random number
        """
        min_value = 10 ** (length - 1)
        max_value = (10 ** length) - 1
        return random.randint(min_value, max_value)

    @staticmethod
    def encrypt_number(number):
        hash_number = hashlib.new("sha256", str(number).encode('utf-8')).hexdigest()
        return hash_number

    @staticmethod
    def minutes_left(time):
        """
        Create a function that returns time in minutes
        """
        now = datetime.now(timezone.utc)
        difference = now - time
        return difference.seconds / 60

    @staticmethod
    def date_diff(date_a=None, date_b=None, type_name='minutes'):
        """
        Create a function that returns time in minutes
        """
        if not date_a:
            date_a = datetime.now(timezone.utc)

        if not date_b:
            date_a = datetime.now(timezone.utc)

        difference = date_a - date_b
        match type_name:
            case 'minutes':
                result = difference.seconds / 60
            case 'seconds':
                result = difference.seconds
            case _:
                raise Exception('Type not found')

        return result

    @staticmethod
    def is_str(v):
        return isinstance(v, str)

    @staticmethod
    def is_json(v):
        return isinstance(v, dict)

    @staticmethod
    def is_dict(v):
        return isinstance(v, dict)

    @staticmethod
    def is_int(v):
        return isinstance(v, int)

    @staticmethod
    def is_list(v):
        return isinstance(v, list)

    @staticmethod
    def serialize_model(model, fields, additional_fields=None):
        if additional_fields is None:
            additional_fields = {}
        sz = serializers.serialize('json', [model], fields=fields)
        original = json.loads(sz)[0]['fields']
        return {**original, **additional_fields}

    @staticmethod
    def now(log=False):
        if log:
            now = datetime.now()
            return now.strftime("%Y-%m-%d %H:%M:%S")
        else:
            return datetime.now(timezone.utc)

    @staticmethod
    def now2(as_string=False):
        if as_string:
            now = datetime.now(timezone.utc)
            return now.isoformat()
        else:
            return datetime.now(timezone.utc)

    @staticmethod
    def can_execute_service(wait_time, date, type_name):
        now = AppUtil.now()
        seconds = AppUtil.date_diff(now, date, type_name)

        available_in = wait_time - seconds if seconds <= wait_time else 0
        status = False if seconds <= wait_time else True
        return {'status': status, 'available_in': available_in}

    @staticmethod
    def sanitize_value(value, date_type=None):
        result = value
        if value:
            match date_type:
                case 'bool':
                    result = AppUtil.sanitize_boolean_value(value)
                case _:
                    # Numeric
                    if value.isnumeric():
                        result = int(value)

                    # Boolean
                    if value == 'true' or value == 'false':
                        result = True if value == 'true' else False

        return result

    @staticmethod
    def sanitize_boolean_value(value):
        if not isinstance(value, bool):
            return True if value.lower() == 'true' or value.lower() == '1' else False
        else:
            return value

    @staticmethod
    def short_name(first_name, last_name):
        parts_a = first_name.split(' ') if first_name else ''
        parts_b = last_name.split(' ') if last_name else ''

        a = parts_a[0] if (AppUtil.is_list(parts_a) and len(parts_a) > 0) else ''
        b = parts_b[0] if (AppUtil.is_list(parts_b) and len(parts_b) > 0) else ''

        return f'{a} {b}'

    @staticmethod
    def full_name(first_name, last_name):
        return f'{first_name} {last_name}'

    @staticmethod
    def generate_resource_name(prefix, record_id, env=None):
        suffix = f'_{env.upper()}' if env and env != 'prd' else ''
        temp = str(record_id).rjust(7, '0')
        return f'{prefix}{temp}{suffix}'

    @staticmethod
    def process_timezone(value):
        minutes = 0

        if value:
            value = int(value)
            minutes = value * -1

        return minutes

    @staticmethod
    def amount_assign(quantity, amount):
        if amount % quantity == 0:
            return amount / quantity
        else:
            return "{:.2f}".format(amount / quantity)

    @staticmethod
    def sum_tuple(tup):
        r = 0
        for item in tup:
            r = r + item
        return r

    @staticmethod
    def change_case(attribute):
        s1 = re.sub('(.)([A-Z][a-z]+)', r'\1_\2', attribute)
        return re.sub('([a-z0-9])([A-Z])', r'\1_\2', s1).lower()

    @staticmethod
    def get_choice_name(choice_class, search):
        output = next((sub for sub in choice_class.CHOICES if search in sub), None)
        return output[1]

    @staticmethod
    def get_url_for_static_images():
        return settings.APP_URL + '/static/images'

    @staticmethod
    def arr_unique(arr):
        return reduce(lambda records, x: records + [x] if x not in records else records, arr, [])
