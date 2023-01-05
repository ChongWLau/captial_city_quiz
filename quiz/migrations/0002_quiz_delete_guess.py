# Generated by Django 4.1.5 on 2023-01-05 14:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('quiz', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Quiz',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('country', models.CharField(max_length=50)),
                ('capital', models.CharField(max_length=50)),
            ],
        ),
        migrations.DeleteModel(
            name='Guess',
        ),
    ]
