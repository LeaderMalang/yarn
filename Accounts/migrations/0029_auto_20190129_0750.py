# Generated by Django 2.0.9 on 2019-01-29 07:50

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Accounts', '0028_auto_20190129_0750'),
    ]

    operations = [
        migrations.AlterField(
            model_name='accounts',
            name='dateTime',
            field=models.DateTimeField(default=datetime.datetime(2019, 1, 29, 7, 50, 41, 889128)),
        ),
    ]
