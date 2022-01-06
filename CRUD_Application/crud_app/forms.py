from django import forms
from django.forms import ModelForm
from .models import Employee


gender=[('male','male'),
        ('female','female')
        ]


class employee_registration_form(forms.ModelForm):

    first_name=forms.CharField(widget=forms.TextInput(attrs={'class':'form-control'}))
    last_name=forms.CharField(widget=forms.TextInput(attrs={'class':'form-control'}))
    email=forms.CharField(widget=forms.TextInput(attrs={'class':'form-control'}))
    gender=forms.ChoiceField(widget=forms.RadioSelect(choices=gender))
    mobile = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control'}))
    class Meta:
        model=Employee
        
        fields='__all__'