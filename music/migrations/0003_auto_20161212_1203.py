# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2016-12-12 12:03
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('music', '0002_auto_20161212_1112'),
    ]

    operations = [
        migrations.AddField(
            model_name='song',
            name='file',
            field=models.BinaryField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='song',
            name='file_type',
            field=models.CharField(choices=[('mp3', 'mp3'), ('wav', 'wav'), ('flac', 'flac')], default='mp3', max_length=7),
        ),
        migrations.AlterField(
            model_name='album',
            name='genre_id',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='music.Genre'),
        ),
        migrations.AlterField(
            model_name='song',
            name='album_id',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='music.Album'),
        ),
    ]
