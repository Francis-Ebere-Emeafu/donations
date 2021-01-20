from django import forms

from convention.models import Attendee, StudentDelegate


class AttendeeForm(forms.ModelForm):

    class Meta:
        model = Attendee
        exclude = []


class StudentDelegateForm(forms.ModelForm):

    class Meta:
        model = StudentDelegate
        exclude = ['when']
