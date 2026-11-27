from django import forms
from .models import Student

class Student_Form(forms.ModelForm):
    class Meta:
        model = Student
        fields = [
            'full_name',
            'course',
            'phone',
            'email',
            'id_card'
        ]