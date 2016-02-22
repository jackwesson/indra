from django import forms


# your_name = forms.CharField(label='Your name', max_length=100)
class NameForm(forms.Form):
    email = forms.EmailField(label='Your email', max_length=50)
    # first = forms.CharField(label='First Name', max_length=50)
    # last = forms.CharField(label='Last Name', max_length=50)
    password = forms.CharField(label='Your password', max_length=50, widget=forms.PasswordInput)    
    
class RegisterForm(forms.Form):
    email = forms.EmailField(label='Your Email', max_length=50)
    first = forms.CharField(label='Your First Name', max_length=50)
    last = forms.CharField(label='Your Last Name', max_length=50)
    password = forms.CharField(label='Your Password', max_length=50, widget=forms.PasswordInput) 
    password_confirmation = forms.CharField(label='Confirm Password', max_length=50, widget=forms.PasswordInput) 