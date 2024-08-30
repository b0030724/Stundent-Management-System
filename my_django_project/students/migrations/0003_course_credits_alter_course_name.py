# Generated by Django 5.0.6 on 2024-08-30 18:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('students', '0002_course_remove_student_age_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='course',
            name='credits',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='course',
            name='name',
            field=models.CharField(max_length=200),
        ),
    ]
