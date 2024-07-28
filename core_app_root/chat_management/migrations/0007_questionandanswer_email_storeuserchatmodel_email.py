# Generated by Django 5.0.6 on 2024-07-23 01:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core_app_root_chat_management', '0006_remove_questionandanswer_user_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='questionandanswer',
            name='email',
            field=models.EmailField(blank=True, max_length=254, null=True, unique=True),
        ),
        migrations.AddField(
            model_name='storeuserchatmodel',
            name='email',
            field=models.EmailField(blank=True, max_length=254, null=True),
        ),
    ]