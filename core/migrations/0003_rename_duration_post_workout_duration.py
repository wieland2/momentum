# Generated by Django 4.2.6 on 2025-03-03 21:33

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0002_post_duration_post_feeling'),
    ]

    operations = [
        migrations.RenameField(
            model_name='post',
            old_name='duration',
            new_name='workout_duration',
        ),
    ]
