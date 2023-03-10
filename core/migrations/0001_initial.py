# Generated by Django 4.1.2 on 2023-01-12 02:36

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Applicant',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=250)),
                ('phone', models.CharField(max_length=15)),
                ('id_number', models.CharField(max_length=50)),
                ('room_type', models.CharField(choices=[('bedsitter', 'bedsitter'), ('single', 'single'), ('1 bedroom', '1 bedroom'), ('2 bedroom', '2 bedroom')], max_length=200)),
            ],
        ),
    ]
