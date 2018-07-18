from django import forms
from .models import Post


class PostForm(forms.ModelForm):
    author = forms.CharField(max_length=50, label='Author', disabled=True)

    class Meta:
        model = Post
        fields = ('title', 'content', 'tags', 'publish', 'active')
        widgets = {
            'title': forms.TextInput(attrs={'placeholder': 'title'}),
            'content': forms.Textarea(attrs={'placeholder': 'content'}),
            'tags': forms.TextInput(attrs={'placeholder': 'e.g. food, restaurant'}),
            'publish': forms.SelectDateWidget()
        }
        labels = {
            'title': 'Title',
            'content': 'Content',
            'tags': 'Tags',
            'publish': 'Publish date',
            'active': 'Active'
        }
