# Generated by Django 3.2.17 on 2023-02-21 05:14

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('lapp', '0002_auto_20230221_1034'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='agent',
            name='post',
        ),
    ]
