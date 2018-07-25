from django import forms
import datetime


class ContactForm(forms.Form):
    email = forms.EmailField(
        label='Email',
        widget=forms.TextInput(attrs={'placeholder': 'email'})
    )
    message = forms.CharField(
        label='Message',
        widget=forms.Textarea(attrs={'placeholder': 'message'})
    )
    date = forms.DateField(
        label='Date',
        initial=datetime.date.today,
        widget=forms.HiddenInput()
    )
