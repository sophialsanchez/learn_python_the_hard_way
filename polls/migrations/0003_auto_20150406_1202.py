# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import picklefield.fields


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0002_room'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='choice',
            name='question',
        ),
        migrations.DeleteModel(
            name='Choice',
        ),
        migrations.DeleteModel(
            name='Question',
        ),
        migrations.RemoveField(
            model_name='room',
            name='next_room',
        ),
        migrations.AddField(
            model_name='room',
            name='dictionary',
            field=picklefield.fields.PickledObjectField(default={'reponse': 'NULL'}, editable=False),
            preserve_default=False,
        ),
    ]
