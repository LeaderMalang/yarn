# Generated by Django 2.0.9 on 2019-01-29 08:43

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Accounts', '0033_auto_20190129_0807'),
    ]

    operations = [
        migrations.AlterField(
            model_name='accounts',
            name='dateTime',
            field=models.DateTimeField(default=datetime.datetime(2019, 1, 29, 8, 43, 41, 499842)),
        ),
    ]
