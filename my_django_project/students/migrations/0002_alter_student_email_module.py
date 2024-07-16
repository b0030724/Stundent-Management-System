# Generated by Django 5.0.6 on 2024-07-11 13:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('students', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='student',
            name='email',
            field=models.EmailField(max_length=100),
        ),
        migrations.CreateModel(
            name='Module',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('code', models.CharField(max_length=10, unique=True)),
                ('name', models.CharField(max_length=100)),
                ('description', models.TextField()),
                ('credits', models.PositiveIntegerField()),
                ('semester', models.CharField(max_length=20)),
                ('instructor', models.CharField(max_length=100)),
                ('students', models.ManyToManyField(related_name='modules', to='students.student')),
            ],
        ),
    ]
