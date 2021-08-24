from django.shortcuts import render
from .models import Person, EmailData
from django.http import JsonResponse
import json
from django.conf import settings 
from django.core.mail import EmailMessage
from django.views.decorators.csrf import csrf_exempt
from .services import archive_records
from django.core.exceptions import ValidationError


# Create your views here.
@csrf_exempt
def send_email(request):
  payload = json.loads(request.body)
  archive_records(payload)

  email = EmailMessage(
    payload['email']['subject'],
    payload['email']['body'],
    settings.EMAIL_HOST_USER,
    [payload['email']['send_to']],
    [payload['email']['bcc']],
  )
  email.send(fail_silently=False)

  return JsonResponse({"status": "sent"})
