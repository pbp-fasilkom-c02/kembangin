# Generated by Django 4.1 on 2022-10-26 14:50

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('report', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='report',
            name='poop',
        ),
    ]