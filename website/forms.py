from django.forms import ModelForm
from website.models import Email_Data

class LeadForm(ModelForm):
    class Meta:
        model = Email_Data
        fields = ['EMAIL_ID']
