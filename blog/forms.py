from django import forms

from .models import Post, Comment, Media

class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ('title', 'text',)
    
class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ('author', 'text',)

class MediaForm(forms.ModelForm):
    class Meta:
        model = Media
        fields = ('description', 'media', )