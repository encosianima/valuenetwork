# -*- coding: utf-8 -*-
# Generated by Django 1.11.29 on 2020-06-01 17:31


from django.db import migrations, models
import easy_thumbnails.fields


class Migration(migrations.Migration):

    dependencies = [
        ('valueaccounting', '0021_auto_20200510_1807'),
    ]

    operations = [
        migrations.AlterField(
            model_name='agentassociation',
            name='state',
            field=models.CharField(choices=[('active', 'active'), ('inactive', 'inactive'), ('potential', 'candidate')], default='active', max_length=12, verbose_name='state'),
        ),
        migrations.AlterField(
            model_name='agentassociationtype',
            name='association_behavior',
            field=models.CharField(blank=True, choices=[('supplier', 'supplier'), ('customer', 'customer'), ('member', 'member'), ('child', 'child'), ('custodian', 'custodian'), ('manager', 'manager'), ('peer', 'peer')], max_length=12, null=True, verbose_name='association behavior'),
        ),
        migrations.AlterField(
            model_name='agentassociationtype',
            name='plural_name',
            field=models.CharField(default='', max_length=128, verbose_name='plural name'),
        ),
        migrations.AlterField(
            model_name='agentassociationtype',
            name='plural_name_ca',
            field=models.CharField(default='', max_length=128, null=True, verbose_name='plural name'),
        ),
        migrations.AlterField(
            model_name='agentassociationtype',
            name='plural_name_en',
            field=models.CharField(default='', max_length=128, null=True, verbose_name='plural name'),
        ),
        migrations.AlterField(
            model_name='agentassociationtype',
            name='plural_name_es',
            field=models.CharField(default='', max_length=128, null=True, verbose_name='plural name'),
        ),
        migrations.AlterField(
            model_name='agenttype',
            name='party_type',
            field=models.CharField(choices=[('individual', 'individual'), ('org', 'organization'), ('network', 'network'), ('team', 'project'), ('community', 'community'), ('company', 'company')], default='individual', max_length=12, verbose_name='party type'),
        ),
        migrations.AlterField(
            model_name='claimevent',
            name='event_effect',
            field=models.CharField(choices=[('+', 'increase'), ('-', 'decrease')], max_length=12, verbose_name='event effect'),
        ),
        migrations.AlterField(
            model_name='economicagent',
            name='photo',
            field=easy_thumbnails.fields.ThumbnailerImageField(blank=True, null=True, upload_to='photos', verbose_name='photo'),
        ),
        migrations.AlterField(
            model_name='economicresource',
            name='photo',
            field=easy_thumbnails.fields.ThumbnailerImageField(blank=True, null=True, upload_to='photos', verbose_name='photo'),
        ),
        migrations.AlterField(
            model_name='economicresourcetype',
            name='behavior',
            field=models.CharField(choices=[('work', 'Type of Work'), ('account', 'Virtual Account'), ('dig_curr', 'Digital Currency'), ('dig_acct', 'Digital Currency Address'), ('dig_wallet', 'Digital Currency Wallet'), ('consumed', 'Produced/Changed + Consumed'), ('used', 'Produced/Changed + Used'), ('cited', 'Produced/Changed + Cited'), ('produced', 'Produced/Changed only'), ('other', 'Other')], default='other', max_length=12, verbose_name='behavior'),
        ),
        migrations.AlterField(
            model_name='economicresourcetype',
            name='inventory_rule',
            field=models.CharField(choices=[('yes', 'Keep inventory'), ('no', 'Not worth it'), ('never', 'Does not apply')], default='yes', max_length=5, verbose_name='inventory rule'),
        ),
        migrations.AlterField(
            model_name='economicresourcetype',
            name='photo',
            field=easy_thumbnails.fields.ThumbnailerImageField(blank=True, null=True, upload_to='photos', verbose_name='photo'),
        ),
        migrations.AlterField(
            model_name='eventtype',
            name='related_to',
            field=models.CharField(choices=[('process', 'process'), ('agent', 'agent'), ('exchange', 'exchange'), ('distribution', 'distribution')], default='process', max_length=12, verbose_name='related to'),
        ),
        migrations.AlterField(
            model_name='eventtype',
            name='relationship',
            field=models.CharField(choices=[('in', 'input'), ('consume', 'consume'), ('use', 'use'), ('out', 'output'), ('cite', 'citation'), ('work', 'work'), ('todo', 'todo'), ('pay', 'payment'), ('receive', 'receipt'), ('expense', 'expense'), ('cash', 'cash input'), ('resource', 'resource contribution'), ('receivecash', 'cash receipt'), ('shipment', 'shipment'), ('distribute', 'distribution'), ('adjust', 'adjust'), ('disburse', 'disburses cash')], default='in', max_length=12, verbose_name='relationship'),
        ),
        migrations.AlterField(
            model_name='eventtype',
            name='resource_effect',
            field=models.CharField(choices=[('+', 'increase'), ('-', 'decrease'), ('+-', 'adjust'), ('x', 'transfer'), ('=', 'no effect'), ('<', 'failure'), ('+~', 'create to change'), ('>~', 'to be changed'), ('~>', 'change')], max_length=12, verbose_name='resource effect'),
        ),
        migrations.AlterField(
            model_name='eventtype',
            name='unit_type',
            field=models.CharField(blank=True, choices=[('area', 'area'), ('length', 'length'), ('quantity', 'quantity'), ('time', 'time'), ('value', 'value'), ('volume', 'volume'), ('weight', 'weight'), ('ip', 'ip'), ('percent', 'percent')], max_length=12, verbose_name='unit type'),
        ),
        migrations.AlterField(
            model_name='help',
            name='page',
            field=models.CharField(choices=[('agent', 'Agent'), ('agents', 'All Agents'), ('all_work', 'All Work'), ('create_distribution', 'Create Distribution'), ('create_exchange', 'Create Exchange'), ('create_sale', 'Create Sale'), ('demand', 'Demand'), ('ed_asmbly_recipe', 'Edit Assembly Recipes'), ('ed_wf_recipe', 'Edit Workflow Recipes'), ('exchange', 'Exchange'), ('home', 'Home'), ('inventory', 'Inventory'), ('labnotes', 'Labnotes Form'), ('locations', 'Locations'), ('associations', 'Maintain Associations'), ('my_work', 'My Work'), ('non_production', 'Non-production time logging'), ('projects', 'Organization'), ('plan_from_recipe', 'Plan from recipe'), ('plan_from_rt', 'Plan from Resource Type'), ('plan_fr_rt_rcpe', 'Plan from Resource Type Recipe'), ('process', 'Process'), ('process_select', 'Process Selections'), ('recipes', 'Recipes'), ('resource_types', 'Resource Types'), ('resource_type', 'Resource Type'), ('supply', 'Supply'), ('non_proc_log', 'Non-process Logging (Work)'), ('proc_log', 'Process Logging (Work)'), ('profile', 'My Profile (Work)'), ('my_history', 'My History (Work)'), ('work_map', 'Map (Work)'), ('work_home', 'Home (Work)'), ('process_work', 'Process (Work)'), ('work_timer', 'Work Now (Work)')], max_length=16, unique=True, verbose_name='page'),
        ),
        migrations.AlterField(
            model_name='order',
            name='order_type',
            field=models.CharField(choices=[('customer', 'Customer order'), ('rand', 'Work order'), ('holder', 'Placeholder order')], default='customer', max_length=12, verbose_name='order type'),
        ),
        migrations.AlterField(
            model_name='unit',
            name='unit_type',
            field=models.CharField(choices=[('area', 'area'), ('length', 'length'), ('quantity', 'quantity'), ('time', 'time'), ('value', 'value'), ('volume', 'volume'), ('weight', 'weight'), ('ip', 'ip'), ('percent', 'percent')], max_length=12, verbose_name='unit type'),
        ),
        migrations.AlterField(
            model_name='valueequation',
            name='percentage_behavior',
            field=models.CharField(choices=[('remaining', 'Remaining percentage'), ('straight', 'Straight percentage')], default='straight', help_text='Remaining percentage uses the %% of the remaining amount to be distributed.  Straight percentage uses the %% of the total distribution amount.', max_length=12, verbose_name='percentage behavior'),
        ),
        migrations.AlterField(
            model_name='valueequationbucket',
            name='filter_method',
            field=models.CharField(blank=True, choices=[('order', 'Order'), ('shipment', 'Shipment or Delivery'), ('dates', 'Date range'), ('process', 'Process')], max_length=12, null=True, verbose_name='filter method'),
        ),
        migrations.AlterField(
            model_name='valueequationbucketrule',
            name='claim_rule_type',
            field=models.CharField(choices=[('debt-like', 'Until paid off'), ('equity-like', 'Forever'), ('once', 'One distribution')], max_length=12, verbose_name='claim rule type'),
        ),
        migrations.AlterField(
            model_name='valueequationbucketrule',
            name='division_rule',
            field=models.CharField(choices=[('percentage', 'Percentage'), ('fifo', 'Oldest first')], max_length=12, verbose_name='division rule'),
        ),
    ]