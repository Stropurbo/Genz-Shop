# Generated by Django 5.2.3 on 2025-07-02 14:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='profile_image',
            field=models.URLField(blank=True, max_length=500, null=True),
        ),
    ]
