# Generated by Django 2.0.9 on 2019-02-21 06:17

import datetime
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Inventory', '0013_auto_20190219_0631'),
    ]

    operations = [
        migrations.DeleteModel(
            name='AddInventory',
        ),
        migrations.AlterField(
            model_name='inventoryin',
            name='agingDate',
            field=models.DateField(verbose_name='Receiving Date'),
        ),
        migrations.AlterField(
            model_name='inventoryin',
            name='dateOfEntry',
            field=models.DateField(default=datetime.datetime(2019, 2, 21, 6, 17, 19, 808999)),
        ),
        migrations.AlterField(
            model_name='inventoryin',
            name='doID',
            field=models.IntegerField(verbose_name='Do No'),
        ),
        migrations.AlterField(
            model_name='inventoryin',
            name='doImage',
            field=models.ImageField(upload_to='doImage/%Y/%m/%d', verbose_name='Do Image'),
        ),
        migrations.AlterField(
            model_name='inventoryin',
            name='invoiceID',
            field=models.IntegerField(verbose_name='Invoice No'),
        ),
        migrations.AlterField(
            model_name='inventoryin',
            name='labReportImage',
            field=models.ImageField(blank=True, upload_to='labReportImage/%Y/%m/%d', verbose_name='Lab Report Image'),
        ),
        migrations.AlterField(
            model_name='inventoryin',
            name='productID',
            field=models.ForeignKey(editable=False, on_delete=django.db.models.deletion.CASCADE, to='Inventory.products'),
        ),
        migrations.AlterField(
            model_name='inventoryin',
            name='purchaseContractID',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Purchase.contracts', verbose_name='Contract ID'),
        ),
        migrations.AlterField(
            model_name='inventoryin',
            name='supplierID',
            field=models.ForeignKey(editable=False, on_delete=django.db.models.deletion.CASCADE, to='Purchase.suppliers', verbose_name='Supplier'),
        ),
        migrations.AlterField(
            model_name='products',
            name='dateModified',
            field=models.DateTimeField(default=datetime.datetime(2019, 2, 21, 6, 17, 19, 808384)),
        ),
    ]