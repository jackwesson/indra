from django import forms


# your_name = forms.CharField(label='Your name', max_length=100)
    
class RegisterForm(forms.Form):
    email = forms.EmailField(label='Your Email', max_length=50)
    name = forms.CharField(label='Your Name', max_length=50)
    # password = forms.CharField(label='Your Password', max_length=50, widget=forms.PasswordInput) 
    # password_confirmation = forms.CharField(label='Confirm Password', max_length=50, widget=forms.PasswordInput) 