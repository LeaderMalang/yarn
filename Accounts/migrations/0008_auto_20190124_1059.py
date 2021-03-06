# Generated by Django 2.0.9 on 2019-01-24 10:59

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Accounts', '0007_auto_20190124_1000'),
    ]

    operations = [
        migrations.CreateModel(
            name='accounts',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('voucherType', models.CharField(default=None, editable=False, max_length=20)),
                ('title', models.CharField(max_length=50)),
                ('description', models.CharField(max_length=50)),
                ('amount', models.IntegerField(max_length=20)),
                ('balance', models.IntegerField(max_length=20)),
                ('date', models.DateField(verbose_name='YY-MM-DD')),
                ('voucherFlag', models.BooleanField(default=False)),
                ('dateTime', models.DateTimeField()),
                ('elementary', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Accounts.elementaryhead')),
                ('head', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Accounts.heads')),
                ('subhead', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Accounts.subheads')),
            ],
        ),
        migrations.CreateModel(
            name='voucher',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20)),
            ],
        ),
        migrations.AddField(
            model_name='accounts',
            name='voucherID',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Accounts.voucher'),
        ),
    ]
