from django.http import HttpResponse,Http404
from apps.account.models import User
from django.shortcuts import get_object_or_404, render, redirect
from apps.account.forms import ProfileForm, ContactUsForm
from django.core.mail import send_mail
from django.conf import settings


def index(request):
    return HttpResponse('Index')

def profile(request, user_id):

    user = get_object_or_404(User, id=user_id)

    if request.method == 'GET':
        form = ProfileForm(instance=user)
    elif request.method == 'POST':
        form = ProfileForm(request.POST, instance=user)
        if form.is_valid():
            form.save()
            return redirect('/account/index')
    context = {'form':form}
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


def _email(request, email_for):
    subject = 'Thank you for your information'
    message = ' it  means a world to us '
    email_from = settings.EMAIL_HOST_USER
    recipient_list = [f'{email_for}', ]
    send_mail(subject, message, email_from, recipient_list)
    return

