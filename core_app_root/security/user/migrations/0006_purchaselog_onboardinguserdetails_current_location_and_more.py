# Generated by Django 5.0.6 on 2024-10-08 03:07

import django.contrib.postgres.fields
import phonenumber_field.modelfields
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core_app_root_security_user', '0005_onboardinguserdetails_user'),
    ]

    operations = [
        migrations.CreateModel(
            name='PurchaseLog',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('apple_purchase_logs', models.JSONField()),
            ],
        ),
        migrations.AddField(
            model_name='onboardinguserdetails',
            name='current_location',
            field=models.CharField(blank=True, max_length=2000, null=True),
        ),
        migrations.AddField(
            model_name='onboardinguserdetails',
            name='language',
            field=models.CharField(blank=True, max_length=1000, null=True),
        ),
        migrations.AddField(
            model_name='onboardinguserdetails',
            name='name',
            field=models.CharField(blank=True, max_length=1000),
        ),
        migrations.AddField(
            model_name='onboardinguserdetails',
            name='phone',
            field=phonenumber_field.modelfields.PhoneNumberField(blank=True, max_length=128, region=None, unique=True),
        ),
        migrations.AddField(
            model_name='onboardinguserdetails',
            name='preference',
            field=django.contrib.postgres.fields.ArrayField(base_field=models.CharField(blank=True, max_length=100000, null=True), blank=True, null=True, size=None),
        ),
        migrations.AddField(
            model_name='onboardinguserdetails',
            name='region',
            field=models.CharField(blank=True, max_length=2000),
        ),
    ]
