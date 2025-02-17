# Generated by Django 4.2.17 on 2024-12-22 15:22

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ("accounts", "0002_profile"),
    ]

    operations = [
        migrations.RenameField(
            model_name="profile",
            old_name="descibtion",
            new_name="description",
        ),
        migrations.AlterField(
            model_name="profile",
            name="user",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE,
                related_name="profile",
                to=settings.AUTH_USER_MODEL,
            ),
        ),
    ]
