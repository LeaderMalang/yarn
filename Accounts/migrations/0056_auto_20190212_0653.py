# Generated by Django 2.0.9 on 2019-02-12 06:53

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Accounts', '0055_auto_20190212_0653'),
    ]

    operations = [
        migrations.AlterField(
            model_name='accounts',
            name='dateTime',
            field=models.DateTimeField(default=datetime.datetime(2019, 2, 12, 6, 53, 55, 66822)),
        ),
    ]