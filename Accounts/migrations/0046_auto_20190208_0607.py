# Generated by Django 2.0.9 on 2019-02-08 06:07

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Accounts', '0045_auto_20190208_0606'),
    ]

    operations = [
        migrations.AlterField(
            model_name='accounts',
            name='dateTime',
            field=models.DateTimeField(default=datetime.datetime(2019, 2, 8, 6, 7, 38, 282008)),
        ),
    ]
