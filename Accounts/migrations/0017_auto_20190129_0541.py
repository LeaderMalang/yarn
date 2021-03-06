# Generated by Django 2.0.9 on 2019-01-29 05:41

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Accounts', '0016_auto_20190128_0752'),
    ]

    operations = [
        migrations.RenameField(
            model_name='elementaryhead',
            old_name='code',
            new_name='codes',
        ),
        migrations.RemoveField(
            model_name='accounts',
            name='amount',
        ),
        migrations.RemoveField(
            model_name='accounts',
            name='head',
        ),
        migrations.RemoveField(
            model_name='accounts',
            name='subhead',
        ),
        migrations.RemoveField(
            model_name='elementaryhead',
            name='head',
        ),
        migrations.AddField(
            model_name='subheads',
            name='fixed',
            field=models.BooleanField(default=False, editable=False),
        ),
        migrations.AlterField(
            model_name='accounts',
            name='balance',
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name='accounts',
            name='dateTime',
            field=models.DateTimeField(default=datetime.datetime(2019, 1, 29, 5, 41, 29, 89844)),
        ),
        migrations.AlterField(
            model_name='elementaryhead',
            name='fixed',
            field=models.BooleanField(default=False, editable=False),
        ),
    ]
