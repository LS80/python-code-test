# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('contenttypes', '0001_initial'),
        ('stream', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='stream',
            options={'ordering': ['-created_at']},
        ),
        migrations.AddField(
            model_name='stream',
            name='content_type',
            field=models.ForeignKey(default=36, to='contenttypes.ContentType'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='stream',
            name='object_id',
            field=models.PositiveIntegerField(default=1),
            preserve_default=False,
        ),
    ]
