from apps.account.views import get_client_ip
from datetime import datetime

class TestMiddleware(object):
    def __init__(self,get_response):
        self.get_response = get_response

    def __call__(self, request):
        with open('./users_ip.txt', 'a') as the_file:
            the_file.write(f'ip:{get_client_ip(request)}, time:{datetime.now()}\n')
        response = self.get_response(request)
        return response
