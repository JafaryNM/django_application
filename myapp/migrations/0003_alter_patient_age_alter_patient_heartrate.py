# Generated by Django 4.0.6 on 2022-07-21 13:44

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0002_patient_heartrate'),
    ]

    operations = [
        migrations.AlterField(
            model_name='patient',
            name='age',
            field=models.IntegerField(validators=[django.core.validators.MinValueValidator(0), django.core.validators.MaxValueValidator(100)]),
        ),
        migrations.AlterField(
            model_name='patient',
            name='heartrate',
            field=models.IntegerField(default=60, validators=[django.core.validators.MinValueValidator(0), django.core.validators.MaxValueValidator(60)]),
        ),
    ]
