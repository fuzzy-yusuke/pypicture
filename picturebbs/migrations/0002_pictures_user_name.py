# Generated by Django 4.1.5 on 2023-01-16 23:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("picturebbs", "0001_initial"),
    ]

    operations = [
        migrations.AddField(
            model_name="pictures",
            name="user_name",
            field=models.CharField(max_length=200, null=True),
        ),
    ]
