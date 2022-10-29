# Generated by Django 4.1.2 on 2022-10-26 23:49

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='iletisim',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('mail', models.CharField(max_length=300)),
                ('message', models.TextField(max_length=5000)),
            ],
        ),
        migrations.CreateModel(
            name='yazilar',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('on_baslik', models.CharField(max_length=100)),
                ('alt_baslik', models.CharField(max_length=300)),
                ('main_image', models.ImageField(blank=True, null=True, upload_to='images/')),
                ('tarih', models.CharField(max_length=50)),
                ('image1', models.ImageField(blank=True, null=True, upload_to='images/')),
                ('yazi1', models.TextField(max_length=5000)),
                ('image2', models.ImageField(blank=True, null=True, upload_to='images/')),
                ('yazi2', models.TextField(max_length=5000)),
                ('image3', models.ImageField(blank=True, null=True, upload_to='images/')),
                ('yaziBenzersizId', models.CharField(max_length=10)),
                ('yazi_path', models.CharField(default='', max_length=100)),
            ],
        ),
    ]
