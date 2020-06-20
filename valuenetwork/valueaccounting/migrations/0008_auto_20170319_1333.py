# -*- coding: utf-8 -*-


from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('valueaccounting', '0007_transfertype_inherit_types'),
    ]

    operations = [
        migrations.AlterField(
            model_name='agenttype',
            name='party_type',
            field=models.CharField(default='individual', max_length=12, verbose_name='party type', choices=[('individual', 'individual'), ('org', 'organization'), ('network', 'network'), ('team', 'project'), ('community', 'community'), ('company', 'company')]),
        ),
    ]
