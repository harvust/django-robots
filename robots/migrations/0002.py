# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('robots', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='CustomDirective',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('directive', models.CharField(max_length=255, verbose_name='directive')),
            ],
            options={
                'verbose_name': 'directive',
                'verbose_name_plural': 'directive',
            },
        ),
    ]
