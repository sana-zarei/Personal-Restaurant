from django import forms
from .models import Comment

class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ('user', 'content')
        widgets = {
            'user': forms.TextInput(attrs={'placeholder': 'Enter Your Name {Required}'}),
            'content': forms.Textarea(attrs={'placeholder': 'Enter Your Comment {Required}'})}