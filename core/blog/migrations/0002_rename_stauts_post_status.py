# Generated by Django 4.2.17 on 2024-12-14 00:02

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("blog", "0001_initial"),
    ]

    operations = [
        migrations.RenameField(
            model_name="post",
            old_name="stauts",
            new_name="status",
        ),
    ]
