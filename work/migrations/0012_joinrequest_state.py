# -*- coding: utf-8 -*-


from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('work', '0011_merge'),
    ]

    operations = [
        migrations.AddField(
            model_name='joinrequest',
            name='state',
            field=models.CharField(default='new', verbose_name='state', max_length=12, editable=False, choices=[('new', 'new'), ('accepted', 'accepted'), ('declined', 'declined')]),
        ),
    ]
