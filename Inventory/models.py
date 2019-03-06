from django.db import models
from datetime import datetime
from django.utils.timezone import now

# Create your models here.
class counts(models.Model):

    name=models.CharField(max_length=30)

    def __str__(self):
        return self.name


class brands(models.Model):

    name=models.CharField(max_length=30,unique=True)

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
        code = '00003-00003-0000' + str(accountID)
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
        productDetailID = productDetails.objects.order_by('id').last()
        products.objects.create(productDetailsID=productDetailID, startingInventory=0, startingPrice=0,
                                inventoryReceived=0, inventoryShipped=0, currentInventory=0, currentPrice=0,
                                minimumRequired=0)
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
    dateModified=models.DateTimeField(default=now)


class inventoryIn(models.Model):


    supplierID=models.ForeignKey('Purchase.suppliers',editable=False,on_delete=models.CASCADE,verbose_name='Supplier')
    productID=models.ForeignKey(products,editable=False,on_delete=models.CASCADE)
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
    dateOfEntry=models.DateField(default=now)
    def __str__(self):
        return str(self.supplierID)



    def save(self, force_insert=False, force_update=False, using=None,
             update_fields=None):
        from Purchase.models import contracts,suppliers
        from Accounts.models import elementaryhead,voucher,accounts
        contract = contracts.objects.values('supplierID', 'productDetailID','ratePerUnit','saleTax','incomeTax','saleTaxwithHeld').filter(id=self.purchaseContractID.id)
        supplier=contract[0].get("supplierID")
        product=contract[0].get("productDetailID")
        productName=productDetails.objects.values('name',).filter(id=product)
        supplierName=suppliers.objects.values('companyName').filter(id=supplier)
        productNameString='CURRENT STOCK('+productName[0].get('name')+')'
        productAccountIDs=elementaryhead.objects.values('id','right','left').filter(name__contains=productNameString)
        supplierAccountIDs=elementaryhead.objects.values('id','right','left').filter(name__contains=supplierName[0].get('companyName'),subhead=10)
        currentStockValue=contract[0].get("ratePerUnit")*self.unitsIn
        totalSaleTax=currentStockValue*(contract[0].get("saleTax")/100)
        accountPayable=currentStockValue+totalSaleTax


        #product Stock Journal Entry


        journalVoucher = voucher.objects.create(name='')
        voucherId = voucher.objects.latest('id')
        lastbalance = accounts.objects.values('balance').filter(id=productAccountIDs[0].get('id'))
        currentLastBalance=0
        if lastbalance :
            currentLastBalance=lastbalance[0].balance -currentStockValue
        else:
            currentLastBalance=currentStockValue
        elementaryInstance=elementaryhead.objects.get(id=productAccountIDs[0].get('id'))
        accounts.objects.create(elementary=elementaryInstance, debit=currentStockValue, credit=0,
                                balance=currentLastBalance, voucherType='JournalVoucher',
                                voucherID=voucherId,date=self.agingDate)
        lastbalanceSaleTax=accounts.objects.values('balance').filter(id=9)
        currentLastBalanceSaleTax=0
        if lastbalanceSaleTax:
            currentLastBalanceSaleTax=lastbalanceSaleTax[0].get('balance')+totalSaleTax
        else:
            currentLastBalanceSaleTax=totalSaleTax
        elementaryInstanceSaleTax=elementaryhead.objects.get(id=9)
        accounts.objects.create(elementary=elementaryInstanceSaleTax, debit=totalSaleTax, credit=0,
                                balance=currentLastBalanceSaleTax, voucherType='JournalVoucher',
                                voucherID=voucherId, date=self.agingDate)

        lastbalanceAccountsPayable=accounts.objects.values('balance').filter(id=supplierAccountIDs[0].get('id'))
        currentLastBalanceAccountsPayable=0
        if lastbalanceAccountsPayable:
            currentLastBalanceAccountsPayable=lastbalanceAccountsPayable[0].get('balance')+accountPayable
        else:
            currentLastBalanceAccountsPayable=accountPayable


        elementaryInstanceAccountPayable=elementaryhead.objects.get(id=supplierAccountIDs[0].get('id'))
        accounts.objects.create(elementary=elementaryInstanceAccountPayable, debit=0, credit=accountPayable,
                                balance=currentLastBalanceAccountsPayable, voucherType='JournalVoucher',
                                voucherID=voucherId, date=self.agingDate)

#creating product Inventory Details
        productInventory=products.objects.filter(productDetailsID=product)
        contractDetail= contractDetails.objects.filter(contractID=self.purchaseContractID.id)
        productDetailInstance = productDetails.objects.get(id=product)
        currentPrice = currentStockValue / self.unitsIn
        if productInventory:
            currentInventory=productInventory[0].get('startingInventory')+productInventory[0].get('inventoryReceived')-productInventory[0].get('inventoryShipped')

            products.objects.create(productDetailsID=productDetailInstance,startingInventory=contractDetail[0].noOfBags
                                    ,inventoryReceived=self.unitsIn,inventoryShipped=0,currentInventory=currentInventory,currentPrice=currentPrice,minimumRequired=0)
        else:
            products.objects.create(productDetailsID=productDetailInstance, startingInventory=contractDetail[0].noOfBags
                                    , inventoryReceived=self.unitsIn, inventoryShipped=0,
                                    currentInventory=self.unitsIn,startingPrice=currentPrice, currentPrice=currentPrice, minimumRequired=0)














        self.supplierID=suppliers.objects.get(id=supplier)
        self.productID=products.objects.get(productDetailsID=product)
        super(inventoryIn,self).save()




class inventoryOut(models.Model):
    customerID = models.ForeignKey('Sale.customers', on_delete=models.CASCADE, verbose_name='Supplier')
    productID = models.ForeignKey(products, on_delete=models.CASCADE,verbose_name='Product')
    saleContractID = models.ForeignKey('Sale.contracts', on_delete=models.CASCADE,verbose_name='Sale Contract')
    unitsOut = models.IntegerField(verbose_name='Units Out',null=True)
    doID = models.IntegerField(verbose_name='Do ID',null=True)
    doImage = models.ImageField(upload_to='doImage/%Y/%m/%d',null=True)
    paymentDays=models.IntegerField(verbose_name='Payment Days',null=True)
    dateOfEntry = models.DateField(default=now)

    def __str__(self):
        return self.customerID

class productsPacking(models.Model):
    name=models.CharField(max_length=25,verbose_name='Name')
    weightPerBag=models.IntegerField(verbose_name='Weight Per Bag',null=True)
    conesPerBag=models.IntegerField(verbose_name='Cones Per Bag',null=True)
    weightPerCone=models.IntegerField(verbose_name='Weight Per Cone',null=True,editable=False)


    def save(self, force_insert=False, force_update=False, using=None,
             update_fields=None):
        self.weightPerCone=self.weightPerBag/self.conesPerBag
        super(productsPacking,self).save()
    def __str__(self):
        return self.name


class productItems(models.Model):
    productDetailID=models.ForeignKey(productDetails,on_delete=models.CASCADE,verbose_name='Product Detail')
    productsPackingID=models.ForeignKey(productsPacking,on_delete=models.CASCADE,verbose_name='Product Packing')
    noOfBags=models.IntegerField(verbose_name='No Of Bags',null=True)
    noOfAdditionalCones=models.IntegerField(verbose_name='No Of Additional Cones',null=True)


class inventoryInDetails(models.Model):
    inventoryInID=models.ForeignKey(inventoryIn,on_delete=models.CASCADE,null=True)
    productsPackingID=models.ForeignKey(productsPacking,on_delete=models.CASCADE,null=True)
    noOfBags=models.IntegerField(verbose_name='No Of Bags',null=True)
    noOfAdditionalCones = models.IntegerField(verbose_name='No Of Additional Cones', null=True)




