# Generated by Django 2.0.9 on 2019-02-14 11:59

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Accounts', '0071_auto_20190214_1114'),
    ]

    operations = [
        migrations.AlterField(
            model_name='accounts',
            name='dateTime',
            field=models.DateTimeField(default=datetime.datetime(2019, 2, 14, 11, 59, 8, 34435)),
        ),
        migrations.AlterField(
            model_name='paymentout',
            name='dateOfentry',
            field=models.DateField(default=datetime.datetime(2019, 2, 14, 11, 59, 8, 35115)),
        ),
    ]
