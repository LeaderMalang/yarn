# Generated by Django 2.0.9 on 2019-02-11 06:00

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Accounts', '0052_auto_20190208_1138'),
    ]

    operations = [
        migrations.AlterField(
            model_name='accounts',
            name='dateTime',
            field=models.DateTimeField(default=datetime.datetime(2019, 2, 11, 6, 0, 26, 655772)),
        ),
    ]
