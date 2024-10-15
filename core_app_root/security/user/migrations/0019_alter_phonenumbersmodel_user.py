# Generated by Django 5.0.6 on 2024-10-11 07:37

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core_app_root_security_user', '0018_remove_onboardinguserdetails_otp_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='phonenumbersmodel',
            name='user',
            field=models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='user_phone_numbers', to=settings.AUTH_USER_MODEL),
        ),
    ]