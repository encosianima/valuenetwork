# -*- coding: utf-8 -*-


from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('valueaccounting', '0003_auto_20160803_1925'),
    ]

    operations = [
        migrations.AlterField(
            model_name='economicevent',
            name='digital_currency_tx_state',
            field=models.CharField(blank=True, max_length=12, null=True, verbose_name='digital currency transaction state', choices=[('new', 'New'), ('pending', 'Pending'), ('broadcast', 'Broadcast'), ('confirmed', 'Confirmed')]),
        ),
    ]
