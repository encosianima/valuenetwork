# -*- coding: utf-8 -*-
# Generated by Django 1.10.7 on 2017-06-11 16:58
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('work', '0030_auto_20170609_1513'),
    ]

    operations = [
        migrations.AddField(
            model_name='project',
            name='resource_type_selection',
            field=models.CharField(choices=[(b'project', 'your project'), (b'all', 'all platform')], default=b'all', max_length=12, verbose_name='resource type selection'),
        ),
    ]
