# Generated by Django 5.0.6 on 2024-10-18 05:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core_app_root_home_management', '0002_rename_homemanamentview_homemanagementview'),
    ]

    operations = [
        migrations.AddField(
            model_name='homemanagementview',
            name='user_location',
            field=models.TextField(blank=True, null=True),
        ),
    ]