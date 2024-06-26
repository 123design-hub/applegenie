# Generated by Django 5.0.6 on 2024-06-26 09:16

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("core_app_root_match_friends", "0003_alter_userattributes_age_and_more"),
    ]

    operations = [
        migrations.CreateModel(
            name="AskQuestionsToMatchModel",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("prompt_in", models.TextField()),
                ("prompt_out", models.TextField()),
            ],
        ),
    ]