# Generated by Django 4.2.3 on 2023-07-19 17:23

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('feedback', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='feedback',
            name='date_added',
        ),
    ]