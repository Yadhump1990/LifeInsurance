# Generated by Django 3.2.17 on 2023-02-28 04:23

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('lapp', '0006_remove_user_request_aid'),
    ]

    operations = [
        migrations.CreateModel(
            name='files',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('file', models.FileField(upload_to='')),
                ('date', models.DateField()),
                ('aid', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='lapp.agent')),
            ],
        ),
    ]