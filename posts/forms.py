from django import forms
from .models import Comment


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['comment']
        widgets = {
            'comment': forms.Textarea(
                attrs={'class': 'contact_text', 'placeholder': 'Write your comment here ...', 'required': 'true'})
        }