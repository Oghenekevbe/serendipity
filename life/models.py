from django.db import models
from django.contrib.auth.models import User
from datetime import datetime


class Doctor(models.Model):
    name = models.OneToOneField(User, on_delete=models.CASCADE)
    phone_number = models.CharField(max_length=20)
    email = models.EmailField()

    def __str__(self):
        return self.name.username

class Patient(models.Model):
    name = models.OneToOneField(User, on_delete=models.CASCADE)
    phone_number = models.CharField(max_length=20)
    email = models.EmailField()
    doctor_notes = models.ManyToManyField(Doctor, through='Notes')

    def __str__(self):
        return self.name.username

class Notes(models.Model):
    doctor = models.ForeignKey(Doctor, on_delete=models.CASCADE)
    patient = models.ForeignKey(Patient, on_delete=models.CASCADE)
    notes = models.TextField()
    date_added = models.DateTimeField(default = datetime.now, blank= True)

    def __str__(self):
        return f"Dr. {self.doctor}'s notes for {self.patient}"
    
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
    
