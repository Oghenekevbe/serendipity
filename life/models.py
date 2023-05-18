from django.db import models
from django.contrib.auth.models import User
from datetime import datetime
from django.urls import reverse


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    phone_number = models.CharField(max_length=20)
    email = models.EmailField()
    
    
    def __str__(self):
        return str(self.user.username)
    
class Doctor(models.Model):
    profile = models.ForeignKey(Profile, on_delete=models.CASCADE, null=True)

    def __str__(self):
        if self.profile:
            return f'Dr. {self.profile.user.username}'
        else:
            return 'Unassigned Doctor'

class Patient(models.Model):
    profile = models.ForeignKey(Profile, on_delete=models.CASCADE, null=True)
    doctor_notes = models.ManyToManyField(Doctor, through='Notes')

    def __str__(self):
        if self.profile:
            return f' {self.profile.user.username}'
        else:
            return 'Unassigned Patient'
    
    def get_absolute_url(self):
        return reverse("profile", kwargs={"pk": self.pk})
    

class Notes(models.Model):
    doctor = models.ForeignKey(Doctor, on_delete=models.CASCADE)
    patient = models.ForeignKey(Patient, on_delete=models.CASCADE)
    notes = models.TextField()
    date_added = models.DateTimeField(default = datetime.now, blank= True)

    def __str__(self):
        return f" {self.doctor}'s notes for {self.patient}"
    
    class Meta:
        ordering = ['date_added']
    

class BlogPost(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    subject = models.CharField(max_length=225)
    body = models.TextField()
    date_added = models.DateTimeField(default = datetime.now, blank= True)

    def __str__(self):
        return f"{self.subject} | {self.author}"
    class Meta:
        ordering = ['date_added']
        
class JournalPost(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    subject = models.CharField(max_length=225)
    body = models.TextField()
    date_added = models.DateTimeField(default = datetime.now, blank= True)

    def __str__(self):
        return f"{self.subject} | {self.author}"
    class Meta:
        ordering = ['date_added']

    def get_absolute_url(self):
        return reverse("journal_list")
        
    
    
class ForumPost(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    subject = models.CharField(max_length=225)
    body = models.TextField()
    date_added = models.DateTimeField(default = datetime.now, blank= True)

    def __str__(self):
        return f"{self.subject} | {self.author}"
    
    class Meta:
        ordering = ['date_added']
    

class Comment(models.Model):
    post = models.ForeignKey(ForumPost, on_delete=models.CASCADE, related_name='comments')
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    body = models.TextField()
    date_added = models.DateTimeField(default = datetime.now, blank= True)

    def __str__(self):
        return f"{self.post.subject} | {self.author}"
    
    class Meta:
        ordering = ['date_added']
    
class Consultation(models.Model):
    doctor = models.ForeignKey(Doctor, on_delete=models.CASCADE, null= True)
    patient = models.ForeignKey(Patient, on_delete=models.CASCADE)
    date = models.DateTimeField(default=datetime.now)
    notes = models.ForeignKey(Notes, on_delete=models.CASCADE, blank=True, null=True)    
    complaint = models.TextField(default='')
    comment = models.ForeignKey('ConsultationComment', on_delete=models.CASCADE, null = True, blank = True, related_name = 'consultation_comments')
    
    def __str__(self):
        return f"{self.patient}'s consultation with {self.doctor}"
    
    class Meta:
        ordering = ['-date']

class ConsultationComment(models.Model):
    consultation = models.ForeignKey(Consultation, on_delete=models.CASCADE, related_name='comments')
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    body = models.TextField()
    date_added = models.DateTimeField(default=datetime.now, blank=True)

    def __str__(self):
        return f"{self.author} commented on {self.consultation}"
