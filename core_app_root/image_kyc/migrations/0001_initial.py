# Generated by Django 5.0.6 on 2024-08-16 00:53

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='UserImageKwc',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user_default_image', models.FileField(upload_to='kyc_images')),
                ('user_real_time_capture', models.FileField(upload_to='kyc_images')),
            ],
        ),
    ]
