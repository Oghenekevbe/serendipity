from django import forms
from .models import Doctor, Notes, Patient, ForumPost, BlogPost, JournalPost, Comment, Profile




class JournalPostForm(forms.ModelForm):
    subject = forms.CharField(
        max_length=225,
        widget=forms.TextInput(attrs={'class': 'form-control'})
    )
    body = forms.CharField(
        widget=forms.Textarea(attrs={'class': 'form-control'})
    )

    class Meta:
        model = JournalPost
        fields = ['subject', 'body']

    def __init__(self, *args, **kwargs):
        self.request = kwargs.pop('request', None)
        super().__init__(*args, **kwargs)
        
