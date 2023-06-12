from django.db import models
from django.contrib.auth.models import User
from datetime import datetime
from django.urls import reverse


class Doctor(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True)

    def __str__(self):
        if self.user:
            return f'Dr. {self.user.username}'
        else:
            return 'Unassigned Doctor'


class Patient(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True)

    def __str__(self):
        if self.user:
            return f'{self.user.username}'
        else:
            return 'Unassigned Patient'

    def get_absolute_url(self):
        return reverse("profile", kwargs={"pk": self.pk})


class Notes(models.Model):
    consultation = models.ForeignKey('Consultation', on_delete=models.CASCADE, null=True)
    doctor = models.ForeignKey(Doctor, on_delete=models.CASCADE)
    notes = models.TextField()
    date_added = models.DateTimeField(default=datetime.now, blank=True)

    def __str__(self):
        if self.consultation_id is not None:
            return f"Notes for Consultation {self.consultation.id}"
        else:
            return 'no consultation id'

    class Meta:
        ordering = ['date_added']


class BlogPost(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    subject = models.CharField(max_length=225)
    body = models.TextField()
    date_added = models.DateTimeField(default=datetime.now, blank=True)

    def __str__(self):
        return f"{self.subject} | {self.author}"

    class Meta:
        ordering = ['date_added']


class JournalPost(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    subject = models.CharField(max_length=225)
    body = models.TextField()
    date_added = models.DateTimeField(default=datetime.now, blank=True)

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
    date_added = models.DateTimeField(default=datetime.now, blank=True)

    def __str__(self):
        return f"{self.subject} | {self.author}"

    class Meta:
        ordering = ['date_added']


class Comment(models.Model):
    post = models.ForeignKey(ForumPost, on_delete=models.CASCADE, related_name='comments')
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    body = models.TextField()
    date_added = models.DateTimeField(default=datetime.now, blank=True)

    def __str__(self):
        return f"{self.post.subject} | {self.author}"

    class Meta:
        ordering = ['date_added']


class Consultation(models.Model):
    doctor = models.ForeignKey(Doctor, on_delete=models.CASCADE, null=True)
    patient = models.ForeignKey(Patient, on_delete=models.CASCADE)
    date = models.DateTimeField(default=datetime.now)
    complaint = models.TextField(default='')
    comment = models.ForeignKey('ConsultationComment', on_delete=models.CASCADE, null=True, blank=True,
                                related_name='consultation_comments')

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
    