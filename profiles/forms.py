from django import forms
from .models import Profile


class ProfileForm(forms.ModelForm):
    '''
    
    '''
    class Meta:
        model = Profile   # model
        exclude = ("user",)  # fields to be excluded


