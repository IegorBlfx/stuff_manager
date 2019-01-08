from django.http import HttpResponse,Http404
from apps.account.models import User
from django.shortcuts import get_object_or_404, render
from apps.account.forms import ProfileForm, ContactUsForm


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
            # TODO return redirect()
    context = {'form':form}
    return render(request, 'account/profile.html', context=context)

def contact_us(request):
    if request.method == 'GET':
        form = ContactUsForm()
    elif request.method == 'POST':
        form = ContactUsForm(request.POST)
        if form.is_valid():
            form.save()
    context = {'form': form}
    return render(request, 'account/contact_us.html', context=context)

def get_client_ip(request):
    x_forwarded_for = request.META.get('HTTP_X_FORWARDED_FOR')
    if x_forwarded_for:
        ip = x_forwarded_for.split(',')[0]
    else:
        ip = request.META.get('REMOTE_ADDR')
    return ip



