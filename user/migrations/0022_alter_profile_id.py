# Generated by Django 5.0.2 on 2024-02-22 17:22

import uuid
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0021_alter_profile_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='id',
            field=models.UUIDField(db_index=True, default=uuid.UUID('d0189029-db34-49de-9550-4f39f24c042e'), editable=False, primary_key=True, serialize=False, unique=True),
        ),
    ]
