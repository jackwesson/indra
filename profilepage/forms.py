from django import forms
from .models import profile, music
from django.forms import ModelForm

class UploadPictureForm(forms.ModelForm):
    class Meta:
        model = profile
        fields = ['profilepicture']
        
            
    
    # title = forms.CharField(max_length=50)
    # file = forms.FileField()

class UploadMusicForm(forms.ModelForm):
    class Meta:
        model = music
        fields = ['examplemusic']