# Generated by Django 2.0.9 on 2019-02-22 06:31

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Inventory', '0014_auto_20190221_0617'),
    ]

    operations = [
        migrations.AlterField(
            model_name='inventoryin',
            name='dateOfEntry',
            field=models.DateField(default=datetime.datetime(2019, 2, 22, 6, 31, 36, 937366)),
        ),
        migrations.AlterField(
            model_name='products',
            name='dateModified',
            field=models.DateTimeField(default=datetime.datetime(2019, 2, 22, 6, 31, 36, 936819)),
        ),
    ]