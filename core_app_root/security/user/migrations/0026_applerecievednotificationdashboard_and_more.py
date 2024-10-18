# Generated by Django 5.0.6 on 2024-10-18 03:44

import django.contrib.postgres.fields
import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core_app_root_security_user', '0025_onboardinguserdetails_current_age'),
    ]

    operations = [
        migrations.CreateModel(
            name='AppleRecievedNotificationDashboard',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('amount_sent', models.IntegerField(blank=True, default=0, null=True)),
                ('receiver_email', models.EmailField(blank=True, max_length=254, null=True)),
                ('sender_email', models.EmailField(blank=True, max_length=254, null=True)),
                ('days_left', models.TextField(blank=True, null=True)),
                ('apple_message_alert', models.TextField(blank=True, null=True)),
                ('location_of_the_gifter', models.TextField(blank=True, null=True)),
                ('interests_of_the_sender', models.TextField(blank=True, null=True)),
                ('education_level_of_sender', models.TextField(blank=True, null=True)),
                ('family_planning_of_sender', models.TextField(blank=True, null=True)),
                ('beliefs', models.TextField(blank=True, null=True)),
                ('accept_button', models.BooleanField(blank=True, default=False, null=True)),
                ('reject_button', models.BooleanField(blank=True, default=False, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='AppleSentDashbaord',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('amount_sent', models.IntegerField(blank=True, default=0, null=True)),
                ('receiver_email', models.EmailField(blank=True, max_length=254, null=True)),
                ('sender_email', models.EmailField(blank=True, max_length=254, null=True)),
                ('days_left', models.TextField(blank=True, null=True)),
                ('apple_message_alert', models.TextField(blank=True, null=True)),
                ('location_of_the_reciever', models.TextField(blank=True, null=True)),
                ('interests_of_the_reciever', models.TextField(blank=True, null=True)),
                ('education_level_of_reciever', models.TextField(blank=True, null=True)),
                ('family_planning_of_reciever', models.TextField(blank=True, null=True)),
                ('beliefs', models.TextField(blank=True, null=True)),
                ('accept_button', models.BooleanField(blank=True, default=False, null=True)),
                ('reject_button', models.BooleanField(blank=True, default=False, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='BookMarkDashboard',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('email_of_user_bookmarked', models.EmailField(blank=True, max_length=254, null=True, unique=True)),
                ('name_of_user_bookmarked', models.TextField()),
                ('profile_picture', models.TextField()),
                ('location', models.TextField()),
                ('interests', models.TextField()),
            ],
        ),
        migrations.RemoveField(
            model_name='user',
            name='customer',
        ),
        migrations.RemoveField(
            model_name='user',
            name='subscription',
        ),
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('bio', models.TextField(blank=True, null=True)),
                ('profile_picture', models.ImageField(blank=True, null=True, upload_to='profile/')),
                ('phone_number', models.CharField(blank=True, max_length=15, null=True)),
                ('strengths', models.TextField(blank=True, null=True)),
                ('weaknesses', models.TextField(blank=True, null=True)),
                ('suggestions_user_emails', django.contrib.postgres.fields.ArrayField(base_field=models.EmailField(blank=True, max_length=254, null=True), blank=True, null=True, size=None)),
                ('onboarding_details', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='core_app_root_security_user.onboardinguserdetails')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
