# Generated by Django 2.0.9 on 2019-02-08 11:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Purchase', '0003_auto_20190208_1125'),
    ]

    operations = [
        migrations.AlterField(
            model_name='users',
            name='buyer',
            field=models.BooleanField(default=None, editable=False, verbose_name='Is Buyer'),
        ),
        migrations.AlterField(
            model_name='users',
            name='supplier',
            field=models.BooleanField(default=None, editable=False, verbose_name='Is Supplier'),
        ),
    ]