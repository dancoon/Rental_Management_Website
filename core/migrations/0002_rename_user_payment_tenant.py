# Generated by Django 4.1.2 on 2022-12-29 07:17

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='payment',
            old_name='user',
            new_name='tenant',
        ),
    ]