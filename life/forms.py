from django import forms
from .models import Doctor, Notes, Patient, ForumPost, BlogPost, JournalPost, Comment, Profile



# class ProfessionalForm(forms.Form):
    
    
#     new_password2 = forms.CharField(max_length=255, widget= forms.PasswordInput(attrs={'class':'form-control', 'type': 'password'}),required=True,)
    
#     class Meta:
#         model = User
#         fields = ('old_password', 'new_password1', 'new_password2')
