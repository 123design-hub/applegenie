# Generated by Django 5.0.6 on 2024-07-23 19:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core_app_root_chat_management', '0009_alter_questionandanswer_email'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userhistory',
            name='email',
            field=models.EmailField(blank=True, max_length=254, null=True),
        ),
    ]