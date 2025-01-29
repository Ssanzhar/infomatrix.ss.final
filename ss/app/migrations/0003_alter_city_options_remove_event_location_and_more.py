# Generated by Django 5.1.4 on 2025-01-07 12:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("app", "0002_event_created_by"),
    ]

    operations = [
        migrations.AlterModelOptions(
            name="city",
            options={"verbose_name_plural": "cities"},
        ),
        migrations.RemoveField(
            model_name="event",
            name="location",
        ),
        migrations.AddField(
            model_name="event",
            name="latitude",
            field=models.FloatField(null=True),
        ),
        migrations.AddField(
            model_name="event",
            name="longitude",
            field=models.FloatField(null=True),
        ),
    ]
