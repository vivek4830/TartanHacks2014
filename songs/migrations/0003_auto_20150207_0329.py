# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('songs', '0002_auto_20150207_0158'),
    ]

    operations = [
        migrations.CreateModel(
            name='Playlist',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('playlistID', models.IntegerField(default=1)),
                ('playlistName', models.CharField(max_length=200)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.AddField(
            model_name='song',
            name='playlist',
            field=models.ForeignKey(default=1, to='songs.Playlist'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='song',
            name='playlistID',
            field=models.IntegerField(default=1),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='song',
            name='playlistPosition',
            field=models.IntegerField(default=1),
            preserve_default=True,
        ),
    ]
