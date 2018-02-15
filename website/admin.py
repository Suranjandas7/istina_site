from django.contrib import admin
from website.models import Email_Data

class Email_Admin(admin.ModelAdmin):
    list_display = ['EMAIL_ID', 'created']

admin.site.register(Email_Data)
# Register your models here.
