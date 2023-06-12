from typing import Any
from django import forms
from django.contrib.auth.models import User
from .models import (
    Doctor,
    Notes,
    Patient,
    ForumPost,
    BlogPost,
    JournalPost,
    Comment,
    Consultation,
    ConsultationComment
)
import random

class JournalPostForm(forms.ModelForm):
    subject = forms.CharField(
        max_length=225, widget=forms.TextInput(attrs={"class": "form-control"})
    )
    body = forms.CharField(widget=forms.Textarea(attrs={"class": "form-control"}))

    class Meta:
        model = JournalPost
        fields = ["subject", "body"]

    def __init__(self, *args, **kwargs):
        self.request = kwargs.pop("request", None)
        super().__init__(*args, **kwargs)


class ConsultationForm(forms.ModelForm):
    complaint = forms.CharField(
        max_length=225, widget=forms.Textarea(attrs={"class": "form-control"})
    )

    class Meta:
        model = Consultation
        fields = ["complaint"]

    def __init__(self, *args, **kwargs):
        self.request = kwargs.pop("request", None)
        super().__init__(*args, **kwargs)

    def save(self, commit=True, *args, **kwargs):
        consultation = super().save(commit=False)

        # Retrieve or create the Patient instance associated with the user
        patient, created = Patient.objects.get_or_create(user=self.request.user)
        consultation.patient = patient

        doctor = random.choice(Doctor.objects.all())
        consultation.doctor = doctor

        if commit:
            consultation.save()
        return consultation


class EditProfileForm(forms.ModelForm):
    username = forms.CharField(max_length=225, widget=forms.TextInput(attrs={"class": "form-control"}))
    first_name = forms.CharField(widget=forms.TextInput(attrs={"class": "form-control"}))
    last_name = forms.CharField(widget=forms.TextInput(attrs={"class": "form-control"}))
    email = forms.CharField(widget=forms.TextInput(attrs={"class": "form-control"}))

    class Meta:
        model = User
        fields = ['username', 'first_name', 'last_name', 'email']

class ConsultationCommentForm(forms.Form):
        body = forms.CharField(
        max_length=225, widget=forms.Textarea(attrs={"class": "form-control"})
    )

        class Meta:
            model = ConsultationComment
            fields = ["body"]
    
class ConsultationNoteForm(forms.ModelForm):
    notes = forms.CharField(
        max_length=225, widget=forms.Textarea(attrs={"class": "form-control"})
    )
    class Meta:
            model = Notes
            fields = ["notes", "doctor"]
    

    
class CommentForm(forms.ModelForm):
    body = forms.CharField(max_length=225, widget=forms.Textarea(attrs={"class": "form-control"}))
    author = forms.ChoiceField(choices=[('anonymous', 'Anonymous'), ('user', 'Use my name')], required=False)

    class Meta:
        model = Comment
        fields = ["body", "author"]

class CommentForm(forms.ModelForm):
    body = forms.CharField(max_length=225, widget=forms.Textarea(attrs={"class": "form-control"}))

    class Meta:
        model = Comment
        fields = ["body"]

    def __init__(self, *args, **kwargs):
        self.request = kwargs.pop('request', None)
        self.post = kwargs.pop('post', None)
        super().__init__(*args, **kwargs)

    def save(self, commit=True, *args, **kwargs):
        comment = super().save(commit=False)
        comment.post = self.post
        comment.author = self.request.user if self.request.user.is_authenticated else None

        if commit:
            comment.save()

        return comment
