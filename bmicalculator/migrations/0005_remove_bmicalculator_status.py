# Generated by Django 4.1.3 on 2022-12-08 18:12

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('bmicalculator', '0004_alter_bmicalculator_bmi_alter_bmicalculator_height_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='bmicalculator',
            name='status',
        ),
    ]
