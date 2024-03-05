# Generated by Django 5.0.2 on 2024-02-22 18:15

import django.db.models.deletion
import uuid
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0023_alter_post_id'),
        ('user', '0027_alter_profile_id'),
    ]

    operations = [
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False, unique=True)),
                ('comment', models.TextField(max_length=200, verbose_name='Yorum')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='Yorum yapılan Tarih')),
                ('owner', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='user.profile', verbose_name='Yorum yapan')),
                ('post', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='posts.post', verbose_name='yorum yapılan Post')),
            ],
            options={
                'verbose_name': 'Yorum',
                'verbose_name_plural': 'Yorumlar',
                'ordering': ['-created_at'],
            },
        ),
    ]
