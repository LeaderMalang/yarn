# Generated by Django 2.0.9 on 2019-02-14 06:57

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Sale', '0004_auto_20190214_0554'),
    ]

    operations = [
        migrations.AlterField(
            model_name='contracts',
            name='dateOfEntry',
            field=models.DateField(default=datetime.datetime(2019, 2, 14, 6, 57, 58, 779286), editable=False),
        ),
    ]
