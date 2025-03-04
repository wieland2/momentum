from django import forms
from .models import Post

class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ["workout", "workout_duration", "feeling", "body"]

        
