# Generated by Django 3.2.6 on 2021-08-14 16:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('donateapp', '0005_ads'),
    ]

    operations = [
        migrations.AddField(
            model_name='ads',
            name='address',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
        migrations.AddField(
            model_name='ads',
            name='description',
            field=models.CharField(blank=True, max_length=1500, null=True),
        ),
    ]