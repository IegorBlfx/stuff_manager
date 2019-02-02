from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.urls import reverse
from django.contrib.auth.decorators import login_required
from apps.account.forms import ProfileForm, ContactUsForm, RequestDayOffForm
from django.conf import settings
from django.core.cache import cache
from django.views.decorators.cache import cache_page
from apps.account.methods import _email


def index(request):
    #from apps.account.tasks import send_email_async

    #send_email_async.delay(subject = 'Thank you for your information',
    #message = ' it  means a world to us ',
    #email_from = settings.EMAIL_HOST_USER,
    #recipient_list = [f'{email_for}', ],)



    from apps.account.models import User
    key = 'user_cache'
    if key in cache:  # check if users exist in cache
        users = cache.get(key)  # get users from cache
        print('11' * 100)
    else:
        users = list(User.objects.all()[:100])  # get users from db
        cache.set(key, users, 15)  # set cache with key='user_cache', write 100 users for 15 seconds
        print('222' * 100)

    return HttpResponse('Index')

# cache.delete(key)  # to delete cache by key
@cache_page(10*60)
def tos(request):
    return HttpResponse('tos')

@cache_page(10*60)
def FAQ(request):
    return HttpResponse('FAQ')


@cache_page(10)
def cache_test(r):
    from time import sleep
    sleep(10)
    return HttpResponse('Cache Test')


@login_required  # profile = login_required(profile)
def profile(request):
    user = request.user
    if request.method == "GET":
        form = ProfileForm(instance=user)
    elif request.method == "POST":
        form = ProfileForm(request.POST, instance=user)
        if form.is_valid():
            form.save()
            return redirect(reverse('account:index'))

    context = {'form': form}
    return render(request, 'account/profile.html', context=context)


def contact_us(request):
    if request.method == 'GET':
        form = ContactUsForm()
    elif request.method == 'POST':
        form = ContactUsForm(request.POST)
        if form.is_valid():
            form.save()
            email = request.POST.get('email_from')
            _email(request, email_for=email)
            return redirect('/account/index/')
    context = {'form': form}
    return render(request, 'account/contact_us.html', context=context)

def get_client_ip(request):
    x_forwarded_for = request.META.get('HTTP_X_FORWARDED_FOR')
    if x_forwarded_for:
        ip = x_forwarded_for.split(',')[0]
    else:
        ip = request.META.get('REMOTE_ADDR')
    return ip

@login_required
def create_request(request):
    user = request.user
    base_form = RequestDayOffForm

    if request.method == "GET":
        form = base_form(user=user)
    elif request.method == "POST":
        form = base_form(request.POST, user=user)
        if form.is_valid():
            form.save()
            return redirect(reverse('account:index'))
    context = {'form': form}
    return render(request, 'account/create-request.html', context=context)




