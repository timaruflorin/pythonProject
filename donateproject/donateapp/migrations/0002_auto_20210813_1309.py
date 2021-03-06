# Generated by Django 3.2.6 on 2021-08-13 10:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('donateapp', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('email', models.EmailField(max_length=60, unique=True)),
                ('username', models.CharField(max_length=30, unique=True)),
                ('is_admin', models.BooleanField(default=False)),
                ('password', models.CharField(max_length=50)),
            ],
        ),
        migrations.DeleteModel(
            name='Account',
        ),
    ]
