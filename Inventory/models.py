from django.db import models
from datetime import datetime


# Create your models here.
class counts(models.Model):

    name=models.CharField(max_length=30)

    def __str__(self):
        return self.name


class brands(models.Model):

    name=models.CharField(max_length=30)

    def __str__(self):
        return self.name


class productDetails(models.Model):
    name=models.CharField(max_length=50,default=None,verbose_name='Product Name')
    label=models.CharField(max_length=50,default=None,verbose_name='Product Label')
    partNumber=models.CharField(max_length=50,default=None,verbose_name='Part Number')
    brand = models.ForeignKey(brands, on_delete=models.CASCADE, verbose_name='Brand')
    count = models.ForeignKey(counts, on_delete=models.CASCADE, verbose_name='Count')
    addInventory = models.BooleanField(blank=True, default=False,
                                       verbose_name='Do you want to add starting Inventory for this product')


    def save(self, force_insert=False, force_update=False, using=None,
             update_fields=None):
        from Accounts.models import elementaryhead
        accountID = elementaryhead.objects.order_by('id').last().id + 1
        code = '00003-00003-000' + str(accountID)
        subhead = 3
        elementaryhead.objects.create(subhead_id=subhead, name='CURRENT STOCK('+self.name+')', fixed=False, codes=code, right=True)
        accountID = elementaryhead.objects.order_by('id').last().id + 1
        subhead = 20
        code = '00003-000020-0000' + str(accountID)
        elementaryhead.objects.create(subhead_id=subhead, name='COGS('+self.name+')', fixed=False, codes=code, right=True)
        accountID = elementaryhead.objects.order_by('id').last().id + 1
        subhead = 24
        code = '00003-000024-0000' + str(accountID)
        elementaryhead.objects.create(subhead_id=subhead, name='REVENUE ('+self.name+')', fixed=False, codes=code, right=True)

        super(productDetails, self).save()
    def __str__(self):
        return self.name

class products(models.Model):
    productDetailsID=models.ForeignKey(productDetails,on_delete=models.CASCADE)
    startingInventory=models.IntegerField(verbose_name='Starting Inventory')
    startingPrice=models.IntegerField(verbose_name='Starting Price')
    inventoryReceived=models.IntegerField(verbose_name='Inventory Received')
    inventoryShipped=models.IntegerField(verbose_name='Inventory Shipped')
    currentInventory=models.IntegerField(verbose_name='Current Inventory')
    currentPrice=models.IntegerField(verbose_name='Current Price')
    minimumRequired=models.IntegerField(verbose_name='Minimum Required')
    dateModified=models.DateTimeField(default=datetime.now())


class inventoryIn(models.Model):


    supplierID=models.ForeignKey('Purchase.suppliers',on_delete=models.CASCADE,verbose_name='Supplier')
    productID=models.ForeignKey(products,on_delete=models.CASCADE)
    purchaseContractID=models.ForeignKey('Purchase.contracts',on_delete=models.CASCADE,verbose_name='Contract ID')
    unitsIn=models.IntegerField(verbose_name='Enter No of Bags')
    MYCHOCIES = (('orginal', 'ORGINAL'), ('dummy', 'DUMMY'))
    doType = models.CharField(blank=True, choices=MYCHOCIES, verbose_name='Select DO Type', max_length=20)
    doID=models.IntegerField(verbose_name='Do No')
    doImage=models.ImageField(upload_to='doImage/%Y/%m/%d',verbose_name='Do Image')
    invoiceID=models.IntegerField(verbose_name='Invoice No')
    invoiceImage=models.ImageField(upload_to='inventoryIn/%Y/%m/%d')
    agingDate=models.DateField(verbose_name='Receiving Date')
    labReportImage = models.ImageField(upload_to='labReportImage/%Y/%m/%d', blank=True,verbose_name='Lab Report Image')
    enterPaymentDays = models.IntegerField(verbose_name='Enter Payment Days', blank=True, default=None)
    dateOfEntry=models.DateField(default=datetime.now())
    def __str__(self):
        return self.supplierID



# class inventoryOut(models.Model):
#     from Sale.models import customers, contracts
#     customerID = models.ForeignKey(customers, on_delete=models.CASCADE, verbose_name='Supplier')
#     productID = models.ForeignKey(products, on_delete=models.CASCADE)
#     saleContractID = models.ForeignKey(contracts, on_delete=models.CASCADE)
#     unitsIn = models.IntegerField(verbose_name='Units In')
#     doID = models.IntegerField(verbose_name='Do ID')
#     doImage = models.ImageField(upload_to='/assets/image')
#     invoiceID = models.IntegerField(verbose_name='Invoice ID')
#     invoiceImage = models.ImageField(upload_to='/assets/image')
#     agingDate = models.DateField()
#     dateOfEntry = models.DateField(default=datetime.now())
#
#     def __str__(self):
#         return self.customerID

class AddInventory(inventoryIn):




    class Meta:
        proxy = True



    def __str__(self):

        return 'Contract={0}'.format(self.purchaseContractID)






