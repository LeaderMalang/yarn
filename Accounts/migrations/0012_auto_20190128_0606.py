# Generated by Django 2.0.9 on 2019-01-28 06:06

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Accounts', '0011_auto_20190125_0713'),
    ]

    operations = [
        migrations.AddField(
            model_name='elementaryhead',
            name='fixed',
            field=models.BooleanField(default=True, editable=False),
        ),
        migrations.AlterField(
            model_name='accounts',
            name='dateTime',
            field=models.DateTimeField(default=datetime.datetime(2019, 1, 28, 6, 6, 26, 660627)),
        ),
    ]
