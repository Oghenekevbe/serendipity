# Generated by Django 3.2.16 on 2023-05-07 18:26

import datetime
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('life', '0006_auto_20230503_2116'),
    ]

    operations = [
        migrations.CreateModel(
            name='Consultation',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date_added', models.DateTimeField(blank=True, default=datetime.datetime.now)),
                ('doctor', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='life.doctor')),
                ('notes', models.ManyToManyField(related_name='consultations', to='life.Notes')),
                ('patient', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='life.patient')),
            ],
        ),
        migrations.CreateModel(
            name='ConsultationComment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('body', models.TextField()),
                ('date_added', models.DateTimeField(blank=True, default=datetime.datetime.now)),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
                ('consultation', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='comments', to='life.consultation')),
            ],
        ),
    ]
