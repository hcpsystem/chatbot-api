from rest_framework.response import Response

from core.utils.app import AppUtil


class APIRender:
    @staticmethod
    def show(message, code=200):
        response = message if AppUtil.is_json(message) else {'message': message}
        return Response(response, status=code)

    @staticmethod
    def error(message, code=400):
        hypermedia = True
        match code:
            case 423:
                return APIRender.show(message, code)
            case 424:
                return APIRender.show(message, code)
            case _:
                return APIRender.show(message, code)

    @staticmethod
    def display(message, code=200):
        return APIRender.show(message, code)

    @staticmethod
    def raw(message, code=200):
        return Response(message, status=code)

    @staticmethod
    def request_errors(errors, code=422):
        message = 'The given data was invalid.'
        found = False

        for attr, value in errors.items():
            if isinstance(value, list) and len(value) > 0 and isinstance(value[0], str):
                message = f'{attr}: {value[0]}'
                found = True

            if found:
                break

        return Response({'message': message, 'errors': errors}, status=code)

    @staticmethod
    def not_found(resource):
        message = f'{resource} not found.'
        return Response({'message': message}, status=404)

