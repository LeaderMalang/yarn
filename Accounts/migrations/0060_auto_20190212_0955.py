# Generated by Django 2.0.9 on 2019-02-12 09:55

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Accounts', '0059_auto_20190212_0931'),
    ]

    operations = [
        migrations.AlterField(
            model_name='accounts',
            name='dateTime',
            field=models.DateTimeField(default=datetime.datetime(2019, 2, 12, 9, 55, 38, 550733)),
        ),
    ]
