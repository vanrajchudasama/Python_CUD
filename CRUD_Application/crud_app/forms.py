from django import forms
from django.forms import ModelForm
from .models import Employee
from django.core import validators
from django.core.exceptions import ValidationError

gender=[('male','Male'),
        ('female','Female')
        ]


class employee_registration_form(forms.ModelForm):

    # def clean_email(self):
    #     data = self.cleaned_data['email']
    #     if "fred@example.com" not in data:
    #         raise ValidationError("You have forgotten about Fred!")

    #     # Always return a value to use as the new cleaned data, even if
    #     # this method didn't change it.
    #     return data
   
                
    class Meta:
        model=Employee
        fields='__all__'
        widgets = {
            'first_name':forms.TextInput(attrs={'class':'form-control'}),
            'last_name':forms.TextInput(attrs={'class':'form-control'}),
            'email':forms.TextInput(attrs={'class':'form-control'}),
            'gender':forms.RadioSelect(choices=gender),
            'mobile':forms.TextInput(attrs={'class':'form-control'})
        }