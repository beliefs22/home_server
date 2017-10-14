# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2017-10-14 14:53
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('video_streamer', '0006_video_video_type'),
    ]

    operations = [
        migrations.AddField(
            model_name='video',
            name='vid',
            field=models.IntegerField(default=1, primary_key=True, serialize=False),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='video',
            name='video_title',
            field=models.CharField(max_length=200),
        ),
    ]
