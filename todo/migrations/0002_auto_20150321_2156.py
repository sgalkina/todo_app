# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('todo', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='task',
            old_name='user',
            new_name='created_by',
        ),
        migrations.AlterField(
            model_name='task',
            name='done',
            field=models.BooleanField(default=False),
            preserve_default=True,
        ),
    ]
