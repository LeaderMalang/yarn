# Generated by Django 2.0.9 on 2019-02-18 06:24

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Inventory', '0011_auto_20190214_1159'),
    ]

    operations = [
        migrations.AlterField(
            model_name='inventoryin',
            name='dateOfEntry',
            field=models.DateField(default=datetime.datetime(2019, 2, 18, 6, 24, 36, 880885)),
        ),
        migrations.AlterField(
            model_name='products',
            name='dateModified',
            field=models.DateTimeField(default=datetime.datetime(2019, 2, 18, 6, 24, 36, 880371)),
        ),
    ]
