# Generated by Django 2.0.9 on 2019-02-13 10:09

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Accounts', '0062_auto_20190213_0512'),
    ]

    operations = [
        migrations.AlterField(
            model_name='accounts',
            name='dateTime',
            field=models.DateTimeField(default=datetime.datetime(2019, 2, 13, 10, 9, 36, 434597)),
        ),
    ]
