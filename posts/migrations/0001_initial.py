# Generated by Django 5.0 on 2024-02-20 19:02

import django.db.models.deletion
import uuid
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('user', '0002_alter_profile_id'),
    ]

    operations = [
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.UUIDField(db_index=True, default=uuid.UUID('6f0ed610-213f-4757-9533-cdb259032a5c'), editable=False, primary_key=True, serialize=False)),
                ('content', models.TextField(verbose_name='Tweet')),
                ('image', models.ImageField(blank=True, null=True, upload_to='posts/', verbose_name='Resim')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='Oluşturulma Tarihi')),
                ('slug', models.SlugField(blank=True, null=True)),
                ('like', models.ManyToManyField(blank=True, related_name='likes', to='user.profile', verbose_name='Beğenenler')),
                ('owner', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='user.profile', verbose_name='Yazar')),
                ('retweet', models.ManyToManyField(blank=True, related_name='retweet', to='user.profile', verbose_name='Retweet')),
                ('save', models.ManyToManyField(blank=True, related_name='saves', to='user.profile', verbose_name='Kaydedenler')),
                ('view', models.ManyToManyField(blank=True, related_name='views', to='user.profile', verbose_name='Görüntüleyenler')),
            ],
            options={
                'verbose_name': 'Tweet',
                'verbose_name_plural': 'Tweetler',
                'ordering': ['-created_at'],
            },
        ),
    ]
