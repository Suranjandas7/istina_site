from django.shortcuts import render
from website.forms import LeadForm
from .models import Email_Data

def homepage(request):

    if request.method == "POST":
        form = LeadForm(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            new_lead = Email_Data()
            new_lead.EMAIL_ID = cd['EMAIL_ID']
            new_lead.save()
            return render(
                request,
                'website/thanks.html'
            )
    else:
        form = LeadForm()
    return render(
        request,
        'website/index.html',
        {'form':LeadForm}
    )
# Create your views here.
