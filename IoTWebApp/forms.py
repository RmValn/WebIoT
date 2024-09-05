from django import forms
from .models import User

class LoginForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['email','password']
        widgets = {
            'email': forms.TextInput(attrs={'placeholder': 'Email'}),
            'password': forms.PasswordInput(attrs={'placeholder': 'Password'}),
        }

class SignUpForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['first_name','last_name','email','password','gender','dob']
        widgets = {
            'first_name': forms.TextInput(attrs={'placeholder': 'First name'}),
            'last_name': forms.TextInput(attrs={'placeholder': 'Last name'}),
            'email': forms.TextInput(attrs={'placeholder': 'Email'}),
            'password': forms.PasswordInput(attrs={'placeholder': 'Password'}),
            'dob': forms.DateInput(format='%dd/%mm/%YYYY',attrs={'type':'date',}),
        }
        
    # first_name = forms.CharField(max_length=30,widget=forms.TextInput(attrs={'placeholder': 'First name'}))
    # last_name = forms.CharField(max_length=30,widget=forms.TextInput(attrs={'placeholder': 'Last name'}))
    # username = forms.CharField(max_length=30,widget=forms.TextInput(attrs={'placeholder': 'Username'}))
    # email = forms.EmailField()
    # password = forms.CharField(label='Password', widget=forms.PasswordInput)
    # dob = forms.DateField()
    # gender = forms.CharField()