# Generated by Django 5.0.6 on 2024-08-31 14:06

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('students', '0005_course_course_code'),
    ]

    operations = [
        migrations.AddField(
            model_name='module',
            name='course',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='modules', to='students.course'),
        ),
    ]
