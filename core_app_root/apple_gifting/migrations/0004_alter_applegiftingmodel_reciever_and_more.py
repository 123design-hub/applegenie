# Generated by Django 5.0.6 on 2024-10-09 11:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core_app_root_apple_gifting', '0003_applegiftingmodel_reciever_accepts_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='applegiftingmodel',
            name='reciever',
            field=models.EmailField(blank=True, max_length=254, null=True),
        ),
        migrations.AlterField(
            model_name='applegiftingmodel',
            name='reciever_accepts',
            field=models.EmailField(blank=True, max_length=254, null=True),
        ),
    ]
