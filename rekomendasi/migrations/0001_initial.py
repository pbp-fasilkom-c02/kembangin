# Generated by Django 4.1.1 on 2022-10-27 04:31

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Rekomendasi',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('gambar', models.URLField()),
                ('nama_barang', models.CharField(max_length=50)),
                ('harga_barang', models.TextField()),
                ('deskripsi', models.TextField()),
                ('url', models.URLField()),
            ],
        ),
    ]
