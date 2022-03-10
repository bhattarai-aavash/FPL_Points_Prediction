from django import forms


class LoginForm(forms.Form):
    username = forms.CharField(label='Username', max_length=30,
                               widget=forms.TextInput(attrs={'class': 'input-box', 'placeholder': 'USERNAME'}))
    password = forms.CharField(
        label='Password', max_length=30, widget=forms.PasswordInput(attrs={'class': 'input-box', 'placeholder': 'PASSWORD'}))


class RegisterForm(forms.Form):
    username = forms.CharField(label='Username', max_length=30,
                               widget=forms.TextInput(attrs={'class': 'input-box', 'placeholder': 'Enter a username'}))
    password = forms.CharField(
        label='Password', max_length=30, widget=forms.PasswordInput(attrs={'class': 'input-box', 'placeholder': 'Enter a password'}))
    email = forms.CharField(label='Email', max_length=30,
                            widget=forms.EmailInput(attrs={'class': 'input-box', 'placeholder': 'Enter your email'}))
    team = forms.CharField(label='Team', max_length=30,
                           widget=forms.TextInput(attrs={'class': 'input-box', 'placeholder': 'Enter your team name'}))
