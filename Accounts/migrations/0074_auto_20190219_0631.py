# Generated by Django 2.0.9 on 2019-02-19 06:31

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Accounts', '0073_auto_20190218_0624'),
    ]

    operations = [
        migrations.AlterField(
            model_name='accounts',
            name='dateTime',
            field=models.DateTimeField(default=datetime.datetime(2019, 2, 19, 6, 31, 43, 529432)),
        ),
        migrations.AlterField(
            model_name='paymentout',
            name='dateOfentry',
            field=models.DateField(default=datetime.datetime(2019, 2, 19, 6, 31, 43, 529982)),
        ),
    ]
