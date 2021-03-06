# Generated by Django 2.0.9 on 2019-02-07 09:43

import datetime
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Accounts', '0043_auto_20190207_0648'),
    ]

    operations = [
        migrations.CreateModel(
            name='brands',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30)),
            ],
        ),
        migrations.CreateModel(
            name='counts',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30)),
            ],
        ),
        migrations.AlterField(
            model_name='accounts',
            name='dateTime',
            field=models.DateTimeField(default=datetime.datetime(2019, 2, 7, 9, 43, 25, 946776)),
        ),
        migrations.AlterField(
            model_name='users',
            name='buyer',
            field=models.BooleanField(default=False, verbose_name='Is Buyer'),
        ),
        migrations.AlterField(
            model_name='users',
            name='city',
            field=models.CharField(max_length=20, verbose_name='City'),
        ),
        migrations.AlterField(
            model_name='users',
            name='companyAddress',
            field=models.CharField(max_length=50, verbose_name='Company Address'),
        ),
        migrations.AlterField(
            model_name='users',
            name='companyFax',
            field=models.IntegerField(verbose_name='Company Fax'),
        ),
        migrations.AlterField(
            model_name='users',
            name='companyName',
            field=models.CharField(max_length=30, verbose_name='Company Name'),
        ),
        migrations.AlterField(
            model_name='users',
            name='companyPhone',
            field=models.IntegerField(verbose_name='Company Phone'),
        ),
        migrations.AlterField(
            model_name='users',
            name='contactPersonName',
            field=models.CharField(max_length=30, verbose_name='Contact Person Name'),
        ),
        migrations.AlterField(
            model_name='users',
            name='elementaryID',
            field=models.ForeignKey(default=None, editable=False, null=True, on_delete=django.db.models.deletion.CASCADE, to='Accounts.elementaryhead', verbose_name='Elementary head'),
        ),
        migrations.AlterField(
            model_name='users',
            name='postalCode',
            field=models.IntegerField(verbose_name='Postal Code'),
        ),
        migrations.AlterField(
            model_name='users',
            name='region',
            field=models.CharField(max_length=20, verbose_name='Region'),
        ),
        migrations.AlterField(
            model_name='users',
            name='supplier',
            field=models.BooleanField(default=False, verbose_name='Is Supplier'),
        ),
    ]
