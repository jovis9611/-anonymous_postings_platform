from django import forms
from .models import model

class PostForm(forms.Form):
       class Meta:
        model = Post
        fields = ('title', 'text',)