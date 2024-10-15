# Generated by Django 5.0.6 on 2024-10-11 04:52

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core_app_root_security_user', '0014_remove_onboardinguserdetails_profile_photo'),
    ]

    operations = [
        migrations.AlterField(
            model_name='onboardinguserdetails',
            name='user',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]
