# Generated by Django 2.0.9 on 2019-02-12 06:45

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Accounts', '0053_auto_20190211_0600'),
    ]

    operations = [
        migrations.AlterField(
            model_name='accounts',
            name='dateTime',
            field=models.DateTimeField(default=datetime.datetime(2019, 2, 12, 6, 45, 11, 377572)),
        ),
    ]
