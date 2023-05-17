# Generated by Django 3.2.17 on 2023-02-21 05:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('lapp', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='agent',
            name='contact',
        ),
        migrations.AddField(
            model_name='agent',
            name='email',
            field=models.EmailField(default=1, max_length=254),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='agent',
            name='experiance',
            field=models.CharField(default=3, max_length=90),
            preserve_default=False,
        ),
    ]
