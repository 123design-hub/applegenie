# Generated by Django 5.0.6 on 2024-10-18 03:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core_app_root_chat_management', '0011_geniequestions_genieresponsetouser_userquestions_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='AnalyseChat',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user_email', models.EmailField(blank=True, max_length=254, null=True)),
            ],
        ),
    ]