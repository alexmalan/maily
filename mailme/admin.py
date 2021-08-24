from django.contrib import admin
from .models import Person, EmailData

# Register your models here.
@admin.register(Person)
class PersonAdmin(admin.ModelAdmin):
    list_display = ('first_name',)

@admin.register(EmailData)
class EmailData(admin.ModelAdmin):
    list_display = ('email_address',)