# Generated by Django 5.0.6 on 2024-08-31 13:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('students', '0004_alter_course_credits'),
    ]

    operations = [
        migrations.AddField(
            model_name='course',
            name='course_code',
            field=models.CharField(blank=True, max_length=10, null=True),
        ),
    ]
