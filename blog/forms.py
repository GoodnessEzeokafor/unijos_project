from django import forms
from django.forms import Textarea
from .models import FileUpload

class FileUploadForm(forms.ModelForm):
    class Meta:
        model = FileUpload
        fields = [
            'title',
            'description',
            'file'   
        ]
        labels = {
            'title': "Enter File Title",
            'description': "Short Description",
            'file':'Upload File'
        }
        # widgets = {
        #     'description': Textarea(attrs={'class':'form-control'})
        # }
        help_texts = {
            'title':'Enter A Descriptive Title',
            'description':'Short Description Of The Uploaded File Atleat 50 words',
            'file':'File To Be Uploaded'
        }
        # error_messages = {

        # }



