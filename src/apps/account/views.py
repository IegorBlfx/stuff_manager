from django.http import HttpResponse,Http404
from apps.account.models import User
from django.shortcuts import get_object_or_404



def index(request):
    return HttpResponse('Index')
def profile(request, user_id):
    user = get_object_or_404(User,id=user_id)
    return HttpResponse(f'{user}')