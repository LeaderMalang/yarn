from django.db import models
# from Purchase.models import contracts

from _datetime import datetime

# Create your models here.
def currency_display(amount):
    return '{:0.2f}'.format(amount) if amount else '0.00'


class heads(models.Model):
    name = models.CharField(max_length=20)
    def __str__(self):
        return self.name


class subheads(models.Model):
    head=models.ForeignKey(heads,on_delete=models.CASCADE)
    name=models.CharField(max_length=30)
    fixed=models.BooleanField(default=False,editable=False)

    def __str__(self):
        return self.name

class elementaryhead(models.Model):
    subhead=models.ForeignKey(subheads,on_delete=models.CASCADE)
    name=models.CharField(max_length=50)
    fixed=models.BooleanField(default=False,editable=False)
    codes=models.CharField(max_length=50,editable=False,default=None)
    left=models.BooleanField(default=False,editable=False)
    right=models.BooleanField(default=False,editable=False)

    def __str__(self):
        return self.name

class voucher(models.Model):
    name=models.CharField(max_length=20,default=None,null=True)

    def __str__(self):
        return ''

class accounts(models.Model):
    voucherID=models.ForeignKey(voucher,on_delete=models.CASCADE)
    elementary=models.ForeignKey(elementaryhead,on_delete=models.CASCADE)
    voucherType=models.CharField(max_length=20,editable=False,default=None)
    title=models.CharField(max_length=50)
    description=models.CharField(max_length=50)
    debit=models.DecimalField(max_digits=15,decimal_places=3,default=None)
    credit=models.DecimalField(max_digits=15,decimal_places=3,default=None)
    balance=models.IntegerField()
    date=models.DateField(format('YY-MM-DD'))
    voucherFlag=models.BooleanField(default=False)
    dateTime=models.DateTimeField(default=datetime.now())



    def __str__(self):
        return self.elementary


# class paymentOut(models.Model):
#     purchaseContractID=models.ForeignKey(contracts,on_delete=models.CASCADE,verbose_name='Purchase Contract')
#     accountID=models.ForeignKey(elementaryhead,on_delete=models.CASCADE,editable=False)
#     chequeNo=models.IntegerField(verbose_name='Cheque No',max_length=20)
#     chequeImage=models.ImageField(upload_to='assets/images/%Y/%m/%d',verbose_name='Cheque Image')
#     depositNo=models.IntegerField(max_length=20,verbose_name='Deposit No')
#     depositImage=models.ImageField(upload_to='assets/images/%Y/%m/%d')
#     totalunits=models.IntegerField(verbose_name='Total Units')
#     dateOfentry=models.DateField(default=datetime.datetime.now())
#     def __str__(self):
#         return self.accountID
#
#
# class paymentOutDetails(models.Model):
#     paymentOutID=models.ForeignKey(paymentOut,on_delete=models.CASCADE)
#     noOfBags=models.IntegerField()
#     noOfAdditionalCone=models.IntegerField()



# class paymentIn(models.Model):
#     saleContractID=models.ForeignKey(contracts,on_delete=models.CASCADE,verbose_name='Sale Contract')
#     accountID=models.ForeignKey(elementaryhead,on_delete=models.CASCADE,editable=False)
#     chequeNo=models.IntegerField(verbose_name='Cheque No',max_length=20)
#     chequeImage=models.ImageField(upload_to='assets/images/%Y/%m/%d',verbose_name='Cheque Image')
#     depositNo=models.IntegerField(max_length=20,verbose_name='Deposit No')
#     depositImage=models.ImageField(upload_to='assets/images/%Y/%m/%d')
#     totalunits=models.IntegerField(verbose_name='Total Units')
#     dateOfentry=models.DateField(default=datetime.datetime.now())
#     def __str__(self):
#         return self.accountID
#
#
# class paymentInDetails(models.Model):
#     paymentOutID=models.ForeignKey(paymentOut,on_delete=models.CASCADE)
#     noOfBags=models.IntegerField()
#     noOfAdditionalCone=models.IntegerField()





