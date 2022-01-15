from django import forms
from .models import Blog,Category
from crispy_forms.helper import FormHelper

class BlogPostForm(forms.ModelForm):
    helper=FormHelper()
    class Meta:
        model=Blog
        fields=['title','content','author','category','thumbnail']

