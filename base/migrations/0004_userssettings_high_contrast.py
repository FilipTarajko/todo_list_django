# Generated by Django 4.1.4 on 2023-01-02 15:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("base", "0003_userssettings_hide_completed_and_more"),
    ]

    operations = [
        migrations.AddField(
            model_name="userssettings",
            name="high_contrast",
            field=models.BooleanField(default=False),
        ),
    ]