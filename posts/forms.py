from django import forms
from . import models


class CreatePosts(forms.ModelForm):
    class Meta:
        model = models.Posts
        fields = ['title', 'thumb']