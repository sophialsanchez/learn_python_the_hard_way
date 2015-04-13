# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0003_auto_20150406_1202'),
    ]

    operations = [
        migrations.AddField(
            model_name='room',
            name='slug',
            field=models.SlugField(default=datetime.datetime(2015, 4, 7, 18, 25, 2, 185264, tzinfo=utc)),
            preserve_default=False,
        ),
    ]
