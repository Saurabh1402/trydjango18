# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('newsletter', '0002_signup_status'),
    ]

    operations = [
        migrations.AlterField(
            model_name='signup',
            name='status',
            field=models.CharField(default=b'd', max_length=1, null=True, blank=True, choices=[(b'd', b'Draft'), (b'p', b'Published'), (b'w', b'Withdrawn')]),
        ),
    ]
