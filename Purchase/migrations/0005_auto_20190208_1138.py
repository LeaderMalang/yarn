# Generated by Django 2.0.9 on 2019-02-08 11:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Purchase', '0004_auto_20190208_1126'),
    ]

    operations = [
        migrations.AddField(
            model_name='contacts',
            name='mobile2',
            field=models.IntegerField(default=None, verbose_name='Another Mobile'),
        ),
        migrations.AlterField(
            model_name='contacts',
            name='mobile1',
            field=models.IntegerField(verbose_name='Mobile'),
        ),
    ]