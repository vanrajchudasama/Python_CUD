from django import forms
from django.forms import ModelForm
from .models import Employee
from django.core import validators
from django.core.exceptions import ValidationError
from django.core.validators import validate_email

gender=[('male','Male'),
        ('female','Female')
        ]


class employee_registration_form(forms.ModelForm):
    email = forms.EmailField(required=True,label='Email',widget=forms.EmailInput(attrs={'id':'email','class':'form-control'}))

    def clean_email(self):
        data = self.cleaned_data['email']
        try:
            validate_email(data)
        except ValidationError as e:
            raise ValidationError("Please enter valid Emain")

        else:
            return data
    class Meta:
        model=Employee
        fields='__all__'
        widgets = {
            'first_name':forms.TextInput(attrs={'class':'form-control'}),
            'last_name':forms.TextInput(attrs={'class':'form-control'}),
            
            'gender':forms.RadioSelect(choices=gender),
            'mobile':forms.TextInput(attrs={'class':'form-control'})
        }