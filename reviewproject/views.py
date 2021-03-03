from django.core.mail import send_mail
from django.http import HttpResponse
from . import settings

def emailfunc(request):
    send_mail('タイトル','本文','settings.DEFAULT_FROM_EMAIL',['iori4321999@gmail.com'],fail_silently=False,)
    return HttpResponse('')