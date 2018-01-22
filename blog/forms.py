from django import forms
from .models import Post, Comment


class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ('author', 'title', 'text', 'video')

        widgets = {
            'title': forms.TextInput(attrs={'class': 'text_input_class'}),
            'text': forms.Textarea(attrs={'class': 'post_content'}),
            'video': forms.TextInput(attrs={'class': 'video_link'})
        }


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ('author', 'text')

        widgets = {
            'author': forms.TextInput(attrs={'class': 'text_input_class'}),
            'text': forms.Textarea(attrs={'class': 'comment_content'})
        }
