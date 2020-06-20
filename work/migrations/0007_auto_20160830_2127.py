# -*- coding: utf-8 -*-


from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('work', '0006_project_skillsuggestion'),
    ]

    operations = [
        migrations.AlterField(
            model_name='project',
            name='joining_style',
            field=models.CharField(default='autojoin', max_length=12, verbose_name='joining style', choices=[('moderated', 'moderated'), ('autojoin', 'autojoin')]),
        ),
        migrations.AlterField(
            model_name='project',
            name='visibility',
            field=models.CharField(default='FCmembers', max_length=12, verbose_name='visibility', choices=[('private', 'private'), ('FCmembers', 'only FC members'), ('public', 'public')]),
        ),
    ]
