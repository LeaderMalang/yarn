# Generated by Django 2.0.9 on 2019-02-14 05:54

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Inventory', '0004_auto_20190214_0534'),
    ]

    operations = [
        migrations.AlterField(
            model_name='products',
            name='dateModified',
            field=models.DateTimeField(default=datetime.datetime(2019, 2, 14, 5, 54, 10, 924099)),
        ),
    ]
