# -*- coding: utf-8 -*-


from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('work', '0005_auto_20160810_1809'),
    ]

    operations = [
        migrations.AddField(
            model_name='membershiprequest',
            name='state',
            field=models.CharField(default='new', verbose_name='state', max_length=12, editable=False, choices=[('new', 'new'), ('accepted', 'accepted'), ('declined', 'declined')]),
        ),
    ]
