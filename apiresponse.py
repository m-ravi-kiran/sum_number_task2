class ApiResponse:
    @staticmethod
    def get_error_response(message='Internal Server Error', status_code=500):
        payload = {'status': status_code, 'error': message}
        return payload, status_code

    @staticmethod
    def get_success_response(result):
        payload = {'status': 200, 'result': result}
        return payload, 200
