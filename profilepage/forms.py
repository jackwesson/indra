from django import forms
from .models import profile, music
from django.forms import ModelForm

class UploadPictureForm(forms.ModelForm):
    class Meta:
        model = profile
        fields = ['profilepicture']
        
            
class UploadMusicForm(forms.ModelForm):
    class Meta:
        model = music
        fields = ['examplemusic']