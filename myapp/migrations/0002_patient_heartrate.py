# Generated by Django 4.0.6 on 2022-07-21 13:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='patient',
            name='heartrate',
            field=models.IntegerField(default=60),
        ),
    ]