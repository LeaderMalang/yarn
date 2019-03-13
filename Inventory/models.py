from django.db import models
from datetime import datetime
from django.utils.timezone import now
from Purchase.models import contracts
# Create your models here.
class counts(models.Model):

    Name=models.CharField(max_length=30)

    def __str__(self):
        return self.Name


class brands(models.Model):

    Name=models.CharField(max_length=30,unique=True)

    def __str__(self):
        return self.Name


class productDetails(models.Model):
    Product_Name=models.CharField(max_length=50,default=None,verbose_name='Product Name')
    Product_Label=models.CharField(max_length=50,default=None,verbose_name='Product Label')
    Part_Number=models.CharField(max_length=50,default=None,verbose_name='Part Number')
    Brand_ID = models.ForeignKey(brands, on_delete=models.CASCADE, verbose_name='Brand')
    Count_ID = models.ForeignKey(counts, on_delete=models.CASCADE, verbose_name='Count')
    addInventory = models.BooleanField(blank=True, default=False,
                                       verbose_name='Do you want to add starting Inventory for this product')


    def save(self, force_insert=False, force_update=False, using=None,
             update_fields=None):
        from Accounts.models import elementaryhead
        accountID = elementaryhead.objects.order_by('id').last().id + 1
        code = '00003-00003-0000' + str(accountID)
        subhead = 3
        elementaryhead.objects.create(subhead_id=subhead, Name='CURRENT STOCK('+self.name+')', Fixed_Flag=False, Account_Codes=code, Right=True)
        accountID = elementaryhead.objects.order_by('id').last().id + 1
        subhead = 20
        code = '00003-000020-0000' + str(accountID)
        elementaryhead.objects.create(subhead_id=subhead, Name='COGS('+self.name+')', Fixed_Flag=False, Account_Codes=code, Right=True)
        accountID = elementaryhead.objects.order_by('id').last().id + 1
        subhead = 24
        code = '00003-000024-0000' + str(accountID)
        elementaryhead.objects.create(subhead_id=subhead, Name='REVENUE ('+self.name+')', Fixed_Flag=False, Account_Codes=code, Right=True)

        super(productDetails, self).save()
        productDetailID = productDetails.objects.order_by('id').last()
        products.objects.create(Product_Details_ID=productDetailID, Starting_Units=0, Starting_Price=0,
                                Units_Received=0, Units_Shipped=0, Current_Units=0, Current_Price=0,
                                Minimum_Required=0)
    def __str__(self):
        return self.Product_Name

class products(models.Model):
    Product_Details_ID=models.ForeignKey(productDetails,on_delete=models.CASCADE)
    Starting_Units=models.IntegerField(verbose_name='Starting Units',default=None)
    Starting_Price=models.IntegerField(verbose_name='Starting Price',default=None)
    Units_Received=models.IntegerField(verbose_name='Units Received',default=None)
    Units_Shipped=models.IntegerField(verbose_name='Units Shipped',default=None)
    Current_Units=models.IntegerField(verbose_name='Current Units',default=None)
    Current_Price=models.IntegerField(verbose_name='Current Price',default=None)
    Minimum_Required=models.IntegerField(verbose_name='Minimum Required',default=None)
    Date_Modified=models.DateTimeField(default=now)


class inventoryIn(models.Model):

    Purchase_Contract_ID=models.ForeignKey('Purchase.contracts',
                                         on_delete=models.CASCADE,verbose_name='Contract ID')
    Units_In=models.IntegerField(verbose_name='Enter No of Bags',null=True)
    MYCHOCIES = (('orginal', 'ORGINAL'), ('dummy', 'DUMMY'))
    Do_Type = models.CharField(blank=True, choices=MYCHOCIES, verbose_name='Select DO Type', max_length=20)
    Do_ID=models.IntegerField(verbose_name='Do No')
    Do_Image=models.ImageField(upload_to='doImage/%Y/%m/%d',verbose_name='Do Image')
    Invoice_ID=models.IntegerField(verbose_name='Invoice No')
    Invoice_Image=models.ImageField(upload_to='inventoryIn/%Y/%m/%d')
    Aging_Date=models.DateField(verbose_name='Receiving Date')
    Lab_Report_Image = models.ImageField(upload_to='labReportImage/%Y/%m/%d', blank=True,verbose_name='Lab Report Image')
    Payment_Days = models.IntegerField(verbose_name='Enter Payment Days', blank=True, default=None)
    Date_Of_Entry=models.DateField(default=now)
    def __str__(self):
        return str(self.Purchase_Contract_ID)



    def save(self, force_insert=False, force_update=False, using=None,
             update_fields=None):
        from Purchase.models import contracts,suppliers,contractDetails
        from Accounts.models import elementaryhead,voucher,accounts
        contract = contracts.objects.values('Supplier_ID', 'Product_Detail_ID','Rate_Per_Unit','Sale_Tax','Income_Tax','Sale_Tax_With_Held').filter(id=self.Purchase_Contract_ID.id)
        supplier=contract[0].get("Supplier_ID")
        product=contract[0].get("Product_Detail_ID")
        productName=productDetails.objects.values('Name',).filter(id=product)
        supplierName=suppliers.objects.values('Company_Name').filter(id=supplier)
        productNameString='CURRENT STOCK('+productName[0].get('Name')+')'
        productAccountIDs=elementaryhead.objects.values('id','Right','Left').filter(Name__contains=productNameString)
        supplierAccountIDs=elementaryhead.objects.values('id','Right','Left').filter(Name__contains=supplierName[0].get('Company_Name'),Subhead_ID=10)
        currentStockValue=contract[0].get("Rate_Per_Unit")*self.Units_In
        totalSaleTax=currentStockValue*(contract[0].get("Sale_Tax")/100)
        accountPayable=currentStockValue+totalSaleTax


        #product Stock Journal Entry


        journalVoucher = voucher.objects.create(Name='')
        voucherId = voucher.objects.latest('id')
        lastbalance = accounts.objects.values('Balance').filter(id=productAccountIDs[0].get('id'))
        currentLastBalance=0
        if lastbalance :
            currentLastBalance=lastbalance[0].Balance -currentStockValue
        else:
            currentLastBalance=currentStockValue
        elementaryInstance=elementaryhead.objects.get(id=productAccountIDs[0].get('id'))
        accounts.objects.create(Elementary_Head_ID=elementaryInstance, Debit=currentStockValue, Credit=0,
                                Balance=currentLastBalance, Voucher_Type='JournalVoucher',
                                Voucher_ID=voucherId,Date_Of_Entry=self.Aging_Date)
        lastbalanceSaleTax=accounts.objects.values('Balance').filter(id=9)
        currentLastBalanceSaleTax=0
        if lastbalanceSaleTax:
            currentLastBalanceSaleTax=lastbalanceSaleTax[0].get('Balance')+totalSaleTax
        else:
            currentLastBalanceSaleTax=totalSaleTax
        elementaryInstanceSaleTax=elementaryhead.objects.get(id=9)
        accounts.objects.create(Elementary_Head_ID=elementaryInstanceSaleTax, Debit=totalSaleTax, Credit=0,
                                Balance=currentLastBalanceSaleTax, Voucher_Type='JournalVoucher',
                                Voucher_ID=voucherId, Date_Of_Entry=self.agingDate)

        lastbalanceAccountsPayable=accounts.objects.values('Balance').filter(id=supplierAccountIDs[0].get('id'))
        currentLastBalanceAccountsPayable=0
        if lastbalanceAccountsPayable:
            currentLastBalanceAccountsPayable=lastbalanceAccountsPayable[0].get('Balance')+accountPayable
        else:
            currentLastBalanceAccountsPayable=accountPayable


        elementaryInstanceAccountPayable=elementaryhead.objects.get(id=supplierAccountIDs[0].get('id'))
        accounts.objects.create(Elementary_Head_ID=elementaryInstanceAccountPayable, Debit=0, Credit=accountPayable,
                                Balance=currentLastBalanceAccountsPayable, Voucher_Type='JournalVoucher',
                                Voucher_ID=voucherId, Date_Of_Entry=self.agingDate)

#creating product Inventory Details
        productInventory=products.objects.filter(Product_Details_ID=product)
        contractDetail= contractDetails.objects.filter(Purchase_Contract_ID=self.Purchase_Contract_ID.id)
        productDetailInstance = productDetails.objects.get(id=product)
        currentPrice = currentStockValue / self.Units_In
        if productInventory:
            currentInventory=productInventory[0].Starting_Units+productInventory[0].Units_Received-productInventory[0].Units_Shipped

            products.objects.create(Product_Details_ID=productDetailInstance,Starting_Units=contractDetail[0].No_Of_Bags
                                    ,Units_Received=self.Units_In,Units_Shipped=0,Current_Units=currentInventory,Current_Price=currentPrice,Minimum_Required=0)
        else:
            products.objects.create(Product_Details_ID=productDetailInstance, Starting_Units=contractDetail[0].No_Of_Bags
                                    , Units_Received=self.Units_In, Units_Shipped=0,
                                    Current_Units=self.Units_In,Starting_Price=currentPrice, Current_Price=currentPrice, Minimum_Required=0)














        self.supplierID=suppliers.objects.get(id=supplier)
        self.productID=product
        super(inventoryIn,self).save()




class inventoryOut(models.Model):
    Customer_ID = models.ForeignKey('Sale.customers', on_delete=models.CASCADE, verbose_name='Supplier')
    Product_ID = models.ForeignKey(products, on_delete=models.CASCADE,verbose_name='Product')
    Sale_Contract_ID = models.ForeignKey('Sale.contracts', on_delete=models.CASCADE,verbose_name='Sale Contract')
    Units_Out = models.IntegerField(verbose_name='Units Out',null=True)
    Do_Id = models.IntegerField(verbose_name='Do ID',null=True)
    Do_Img = models.ImageField(upload_to='doImage/%Y/%m/%d',null=True)
    Payment_Days=models.IntegerField(verbose_name='Payment Days',null=True)
    Date_Of_Entry = models.DateField(default=now)

    def __str__(self):
        return self.Customer_ID

class productsPacking(models.Model):
    Name=models.CharField(max_length=25,verbose_name='Name')
    Weight_Per_Bag=models.IntegerField(verbose_name='Weight Per Bag',null=True)
    Cones_Per_Bag=models.IntegerField(verbose_name='Cones Per Bag',null=True)
    Weight_Per_Cone=models.IntegerField(verbose_name='Weight Per Cone',null=True,editable=False)


    def save(self, force_insert=False, force_update=False, using=None,
             update_fields=None):
        self.Weight_Per_Cone=self.Weight_Per_Bag/self.Cones_Per_Bag
        super(productsPacking,self).save()
    def __str__(self):
        return self.Name


class productItems(models.Model):
    Product_Detail_ID=models.ForeignKey(productDetails,on_delete=models.CASCADE,verbose_name='Product Detail')
    Products_Packing_ID=models.ForeignKey(productsPacking,on_delete=models.CASCADE,verbose_name='Product Packing')
    No_Of_Bags=models.IntegerField(verbose_name='No Of Bags',null=True)
    No_Of_Additional_Cones=models.IntegerField(verbose_name='No Of Additional Cones',null=True)


class inventoryInDetails(models.Model):
    Inventory_In_ID=models.ForeignKey(inventoryIn,on_delete=models.CASCADE,null=True)
    Products_Packing_ID=models.ForeignKey(productsPacking,on_delete=models.CASCADE,null=True)
    No_Of_Bags=models.IntegerField(verbose_name='No Of Bags',null=True)
    No_Of_Additional_Cones = models.IntegerField(verbose_name='No Of Additional Cones', null=True)





