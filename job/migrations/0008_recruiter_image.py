# Generated by Django 4.2.5 on 2024-03-13 05:20

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("job", "0007_remove_recruiter_image"),
    ]

    operations = [
        migrations.AddField(
            model_name="recruiter",
            name="image",
            field=models.FileField(null=True, upload_to=""),
        ),
    ]
