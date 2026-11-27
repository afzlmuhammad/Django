from django import forms
from .models import Teacher

class Teacher_Form(forms.ModelForm):
    class Meta:
        model = Teacher
        fields = [
            'fname',
            'lname',
            'subject',
            'experience',
            'profile_photo'
        ]