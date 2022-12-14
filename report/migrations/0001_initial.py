# Generated by Django 4.1.3 on 2022-11-01 12:19

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Report',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField(default=django.utils.timezone.now)),
                ('name', models.CharField(max_length=255)),
                ('height', models.IntegerField()),
                ('weight', models.IntegerField()),
                ('eat', models.CharField(max_length=15)),
                ('drink', models.CharField(max_length=15)),
                ('poop', models.CharField(max_length=15)),
                ('issue', models.TextField()),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
