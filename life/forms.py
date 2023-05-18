from django import forms
from .models import Doctor, Notes, Patient, ForumPost, BlogPost, JournalPost, Comment, Profile, Consultation




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
        

class ConsultationForm(forms.ModelForm):
    complaint = forms.CharField(max_length=225, widget=forms.Textarea(attrs={'class': 'form-control'}))

    class Meta:
        model = Consultation
        fields = ['complaint']

    def __init__(self, *args, **kwargs):
        self.request = kwargs.pop('request', None)
        super().__init__(*args, **kwargs)

    def save(self, commit=True, *args, **kwargs):
        consultation = super().save(commit=False)

        # Retrieve or create the Patient instance associated with the user
        patient, _ = Patient.objects.get_or_create(profile__user=self.request.user)
        consultation.patient = patient

        if commit:
            consultation.save()
        return consultation
