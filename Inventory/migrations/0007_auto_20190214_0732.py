# Generated by Django 2.0.9 on 2019-02-14 07:32

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Inventory', '0006_auto_20190214_0657'),
    ]

    operations = [
        migrations.AlterField(
            model_name='products',
            name='dateModified',
            field=models.DateTimeField(default=datetime.datetime(2019, 2, 14, 7, 32, 44, 991554)),
        ),
    ]
