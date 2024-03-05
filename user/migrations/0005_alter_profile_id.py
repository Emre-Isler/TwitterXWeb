# Generated by Django 5.0.2 on 2024-02-22 17:06

import uuid
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0004_alter_profile_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='id',
            field=models.UUIDField(db_index=True, default=uuid.UUID('fb08749f-02b9-487a-b5fe-01b28661100c'), editable=False, primary_key=True, serialize=False),
        ),
    ]
