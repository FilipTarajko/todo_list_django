# Generated by Django 4.1.4 on 2023-01-02 20:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("base", "0004_userssettings_high_contrast"),
    ]

    operations = [
        migrations.AlterField(
            model_name="userssettings",
            name="high_contrast",
            field=models.BooleanField(default=True),
        ),
    ]
