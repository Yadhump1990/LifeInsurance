# Generated by Django 3.2.17 on 2023-02-22 06:56

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('lapp', '0005_user_request_aid'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='user_request',
            name='aid',
        ),
    ]
