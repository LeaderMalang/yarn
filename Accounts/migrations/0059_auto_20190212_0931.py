# Generated by Django 2.0.9 on 2019-02-12 09:31

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Accounts', '0058_auto_20190212_0930'),
    ]

    operations = [
        migrations.AlterField(
            model_name='accounts',
            name='dateTime',
            field=models.DateTimeField(default=datetime.datetime(2019, 2, 12, 9, 31, 31, 471688)),
        ),
    ]
