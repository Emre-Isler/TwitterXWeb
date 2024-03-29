# Generated by Django 5.0 on 2024-02-19 18:52

import django.db.models.deletion
import uuid
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('id', models.UUIDField(db_index=True, default=uuid.UUID('714381fb-f9d5-4933-8e47-f6dda275e66a'), editable=False, primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=200, verbose_name='İsim Soyisim')),
                ('bio', models.TextField(blank=True, default='Merhaba, Ben twitter kullanıyorum.', null=True, verbose_name='Hakkımda')),
                ('image', models.ImageField(upload_to='profiles/', verbose_name='Profil Resmi')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('slug', models.SlugField(blank=True, editable=False, null=True)),
                ('follow', models.ManyToManyField(blank=True, to='user.profile', verbose_name='Takip edilenler')),
                ('follower', models.ManyToManyField(blank=True, to='user.profile', verbose_name='Takipçiler')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'Profil',
                'verbose_name_plural': 'Profiller',
                'ordering': ['-created_at'],
            },
        ),
    ]
