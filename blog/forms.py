from django import forms
from .models import Comment


class CommentForm(forms.ModelForm):
    """
    Class which is a form so users can comment on posts
    """
    class Meta:
        """
        Meta class within CommentForm to define additional attributes.

        Attributes:
        model (class): The model associated with the form (Comment).
        fields (tuple): The fields to include in the form (only 'body').
        """
        model = Comment
        fields = ('body',)