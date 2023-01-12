# Generated by Django 4.1.2 on 2023-01-12 11:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tenants', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='PaymentStatement',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tenant_name', models.CharField(max_length=250)),
                ('mode_of_payment', models.CharField(max_length=50)),
                ('amount', models.PositiveBigIntegerField()),
                ('payment_for', models.CharField(max_length=250)),
                ('date', models.DateField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='TenantFeedback',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tenant_name', models.CharField(max_length=250)),
                ('feedback', models.TextField()),
                ('date', models.DateField(auto_now=True)),
            ],
        ),
    ]
