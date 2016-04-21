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
    eventname = forms.CharField('eventname')
    date = forms.DateInput('date')
    price = forms.DecimalField('price', max_digits=3, decimal_places=2)
    