# Generated by Django 4.1.5 on 2023-01-04 17:33

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Guess',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('country_text', models.CharField(max_length=200)),
                ('capital_text', models.CharField(max_length=200)),
            ],
        ),
    ]
