# -*- coding: utf-8 -*-
# Generated by Django 1.10.7 on 2017-09-07 22:53
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion
import mptt.fields


class Migration(migrations.Migration):

    dependencies = [
        ('general', '0008_auto_20170510_0705'),
    ]

    operations = [
        migrations.CreateModel(
            name='rel_Job_Jobs',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
            options={
                'verbose_name': 'J_job',
                'verbose_name_plural': 'Related jobs',
            },
        ),
        migrations.AlterField(
            model_name='job',
            name='clas',
            field=models.CharField(blank=True, help_text='Django model or python class associated to the Job', max_length=50, verbose_name='Clas'),
        ),
        migrations.AddField(
            model_name='rel_job_jobs',
            name='job1',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='rel_jobs1', to='general.Job'),
        ),
        migrations.AddField(
            model_name='rel_job_jobs',
            name='job2',
            field=mptt.fields.TreeForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='rel_jobs2', to='general.Job'),
        ),
        migrations.AddField(
            model_name='rel_job_jobs',
            name='relation',
            field=mptt.fields.TreeForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='jo_job+', to='general.Relation'),
        ),
        migrations.AddField(
            model_name='job',
            name='jobs',
            field=models.ManyToManyField(blank=True, through='general.rel_Job_Jobs', to='general.Job', verbose_name='related Skills'),
        ),
    ]