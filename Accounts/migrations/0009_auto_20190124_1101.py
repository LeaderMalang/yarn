# Generated by Django 2.0.9 on 2019-01-24 11:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Accounts', '0008_auto_20190124_1059'),
    ]

    operations = [
        migrations.AlterField(
            model_name='voucher',
            name='name',
            field=models.CharField(default=None, max_length=20),
        ),
    ]
