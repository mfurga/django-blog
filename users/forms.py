from django.contrib.auth import authenticate
from django.contrib.auth.models import User
from django import forms


class SigninForm(forms.Form):
    username = forms.CharField(
        max_length=50,
        label='Username',
        widget=forms.TextInput(attrs={'placeholder': 'username'})
    )
    password = forms.CharField(
        max_length=50,
        label='Password',
        widget=forms.PasswordInput(attrs={'placeholder': 'password'})
    )

    def clean(self):
        username = self.cleaned_data.get('username')
        password = self.cleaned_data.get('password')
        user = authenticate(username=username, password=password)
        if user is None:
            raise forms.ValidationError('Username or password incorrect.')
        return super(SigninForm, self).clean()


class RegisterForm(forms.Form):
    username = forms.CharField(
        max_length=50,
        label='Username',
        widget=forms.TextInput(attrs={'placeholder': 'username'})
    )
    password = forms.CharField(
        max_length=50,
        label='Password',
        widget=forms.PasswordInput(attrs={'placeholder': 'password'})
    )
    password_repeat = forms.CharField(
        max_length=50,
        label='Password repeat',
        widget=forms.PasswordInput(attrs={'placeholder': 'password repeat'})
    )

    def clean_username(self):
        username = self.cleaned_data.get('username')
        if User.objects.filter(username=username).count():
            raise forms.ValidationError('This username is already exists.')
        return username

    def clean_password(self):
        password = self.cleaned_data.get('password')
        if len(password) < 8:
            raise forms.ValidationError('Password must contain min. 8 characters.')
        return password

    def clean_password_repeat(self):
        password = self.cleaned_data.get('password')
        password_repeat = self.cleaned_data.get('password_repeat')
        if password != password_repeat:
            raise forms.ValidationError('Passwords are not the same.')
        return password_repeat


class BlogSettingsForm(forms.Form):
    num_pages = forms.IntegerField()
