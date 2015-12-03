# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('demo1', '0002_auto_20151202_2342'),
    ]

    operations = [
        migrations.AddField(
            model_name='article',
            name='optional_image',
            field=models.ImageField(default=1, upload_to=b''),
            preserve_default=False,
        ),
    ]
