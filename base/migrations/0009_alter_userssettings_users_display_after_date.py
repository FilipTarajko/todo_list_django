# Generated by Django 4.1.4 on 2023-01-02 23:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("base", "0008_alter_userssettings_users_display_after_date"),
    ]

    operations = [
        migrations.AlterField(
            model_name="userssettings",
            name="users_display_after_date",
            field=models.DateTimeField(auto_now_add=True),
        ),
    ]
