# Generated by Django 4.1.5 on 2023-02-06 13:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("picturebbs", "0003_pictures_image"),
    ]

    operations = [
        migrations.AlterField(
            model_name="pictures",
            name="image",
            field=models.ImageField(blank=True, null=True, upload_to="media/"),
        ),
    ]