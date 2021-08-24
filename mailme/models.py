from django.db import models


# Create your models here.
class Person(models.Model):
  first_name = models.CharField(max_length=200)
  last_name = models.CharField(max_length=200)
  email = models.CharField(max_length=200)

  def __str__(self):
      return f'{self.name}'


class EmailData(models.Model):
  user = models.ForeignKey(Person, on_delete=models.CASCADE)
  subject = models.CharField(max_length=200)
  bcc = models.EmailField()
  email_address = models.EmailField()
  send_to = models.EmailField()
  body = models.TextField()

  def __str__(self):
      return f'{self.name}'
