from django import forms
from django.http import HttpResponseRedirect
from django.shortcuts import render
from .models import Booking

class EventForm(forms.ModelForm):
    class Meta:
        model = Booking
        fields = ['eventName', 'eventDate', 'eventTime', 'eventLocation', 'boothSelect', 'additionalInfo']

def book_event(request):
    if request.method == 'POST':
        form = EventForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/thanks/')
    else:
        form = EventForm()
    return render(request, 'book_event.html', {'form': form})

class AdminLoginForm(forms.Form):
    username = forms.CharField(label='Username')
    password = forms.CharField(label='Password', widget=forms.PasswordInput)

class AssignStaffForm(forms.Form):
    staff = forms.ChoiceField(
        choices=[('', 'Select a staff member'), ('Staff Member 1', 'Staff Member 1'),
                 ('Staff Member 2', 'Staff Member 2'), ('Staff Member 3', 'Staff Member 3'),
                 ('Staff Member 4', 'Staff Member 4'), ('Staff Member 5', 'Staff Member 5')],
        required=False
    )

