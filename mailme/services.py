from .models import Person, EmailData
from django.core.exceptions import ValidationError


def archive_records(payload):
  """
  The aim of this method is to insert the user details 
  inside the database in order for us to keep an archive of the usages
  """
  if payload is None:
    raise ValidationError("Empty payload")
  if payload['email']['subject'] is None:
    raise ValidationError("Subject is missing")
  if payload['email']['body'] is None:
    raise ValidationError("Empty email body")
  if [payload['email']['send_to']] is None:
    raise ValidationError("Sender address missing")
  
  new_person = Person(first_name=payload["first_name"], last_name=payload["last_name"], email=payload["email"]["send_to"])
  new_person.save()

  new_email = EmailData(subject=payload["email"]["subject"], bcc=payload["email"]["bcc"], email_address=payload["email"]["email_address"], send_to=payload["email"]["send_to"], body=payload["email"]["body"], user=new_person)
  new_email.save()
