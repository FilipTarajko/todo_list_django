# Generated by Django 4.1.4 on 2023-01-02 23:18

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ("base", "0006_task_deadline"),
    ]

    operations = [
        migrations.AlterModelOptions(
            name="task", options={"ordering": ["complete", "-deadline", "created"]},
        ),
        migrations.AddField(
            model_name="userssettings",
            name="users_display_after_date",
            field=models.DateTimeField(
                auto_now_add=True, default=django.utils.timezone.now
            ),
            preserve_default=False,
        ),
    ]
