# -*- coding: utf-8 -*-


from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('valueaccounting', '0002_auto_20160706_2026'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='location',
            options={'ordering': ('name',)},
        ),
        migrations.AlterField(
            model_name='agentassociation',
            name='state',
            field=models.CharField(default='active', max_length=12, verbose_name='state', choices=[('active', 'active'), ('inactive', 'inactive'), ('potential', 'candidate')]),
        ),
        migrations.AlterField(
            model_name='agentassociationtype',
            name='association_behavior',
            field=models.CharField(blank=True, max_length=12, null=True, verbose_name='association behavior', choices=[('supplier', 'supplier'), ('customer', 'customer'), ('member', 'member'), ('child', 'child'), ('custodian', 'custodian'), ('manager', 'manager'), ('peer', 'peer')]),
        ),
        migrations.AlterField(
            model_name='valueequation',
            name='percentage_behavior',
            field=models.CharField(default='straight', help_text='Remaining percentage uses the %% of the remaining amount to be distributed.  Straight percentage uses the %% of the total distribution amount.', max_length=12, verbose_name='percentage behavior', choices=[('remaining', 'Remaining percentage'), ('straight', 'Straight percentage')]),
        ),
    ]
