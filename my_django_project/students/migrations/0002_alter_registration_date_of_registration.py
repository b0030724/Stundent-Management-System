# Generated by Django 5.0.6 on 2024-08-16 23:48

import django.utils.timezone
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('students', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='registration',
            name='date_of_registration',
            field=models.DateField(default=django.utils.timezone.now),
        ),
    ]
