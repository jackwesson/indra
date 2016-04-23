from django import forms
from .models import Profile, music, description
from django.forms import ModelForm

class UploadPictureForm(forms.Form):
   pic = forms.ImageField()
        
            
class UploadMusicForm(forms.ModelForm):
    class Meta:
        model = music
        fields = ['examplemusic']
        
class UploadBlurbForm(forms.Form):
    blurb = forms.CharField()
    
class UploadEventForm(forms.Form):
    eventname = forms.CharField(max_length = 100)
    event_desc = forms.CharField(max_length = 200)
    date = forms.DateInput()
    price = forms.DecimalField(max_digits=3, decimal_places=2)
    