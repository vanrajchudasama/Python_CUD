from django import forms
from django.forms import ModelForm
from .models import Employee
from django.core import validators
import re

gender=[('male','Male'),
        ('female','Female')
        ]

regex = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b'
mo = r'\b[0-9]{10}\b'
class employee_registration_form(forms.ModelForm):

    E_email = forms.CharField(label='Email',widget=forms.EmailInput(attrs={'class':'form-control'}))
   
    mobile = forms.CharField(widget=forms.NumberInput(attrs={'class':'form-control'}))
    def clean_E_email(self):
        data = self.cleaned_data['E_email']
        if(re.fullmatch(regex, data)):
        
            print(data)
        else:
            raise forms.ValidationError("Please enter valid email address")

        # Always return a value to use as the new cleaned data, even if
        # this method didn't change it.
        return data
    def clean_mobile(self):
        mobile = self.cleaned_data['mobile']
        if (re.fullmatch(mo, mobile)):
            return mobile
        else:
            raise forms.ValidationError("Please Enter valid number")
                
    class Meta:
        model=Employee
        fields='__all__'
        widgets = {
            'first_name':forms.TextInput(attrs={'class':'form-control'}),
            'last_name':forms.TextInput(attrs={'class':'form-control'}),
            'gender':forms.RadioSelect(choices=gender),
        }