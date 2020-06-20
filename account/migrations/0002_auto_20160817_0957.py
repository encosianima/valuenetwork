# -*- coding: utf-8 -*-


from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='account',
            name='language',
            field=models.CharField(default='en', max_length=10, verbose_name='language', choices=[('en', 'English'), ('es', 'espa\xf1ol')]),
        ),
    ]
