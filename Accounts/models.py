from django.db import models

from _datetime import datetime
from django.utils.timezone import now

# Create your models here.
def currency_display(amount):
    return '{:0.2f}'.format(amount) if amount else '0.00'


class heads(models.Model):
    Name = models.CharField(max_length=20)
    def __str__(self):
        return self.Name


class subheads(models.Model):
    Head_ID=models.ForeignKey(heads,on_delete=models.CASCADE)
    Name=models.CharField(max_length=30)
    Fixed_Flag=models.BooleanField(default=False,editable=False)

    def __str__(self):
        return self.Name

class elementaryhead(models.Model):
    Subhead_ID=models.ForeignKey(subheads,on_delete=models.CASCADE)
    Name=models.CharField(max_length=50)
    Fixed_Flag=models.BooleanField(default=False,editable=False)
    Account_Codes=models.CharField(max_length=50,editable=False,default=None)
    Left=models.BooleanField(default=False,editable=False)
    Right=models.BooleanField(default=False,editable=False)

    def __str__(self):
        return self.name

class voucher(models.Model):
    Name=models.CharField(max_length=20,default=None,null=True)

    def __str__(self):
        return ''

class accounts(models.Model):
    Voucher_ID=models.ForeignKey(voucher,on_delete=models.CASCADE)
    Elementary_Head_ID=models.ForeignKey(elementaryhead,on_delete=models.CASCADE)
    Voucher_Type=models.CharField(max_length=20,editable=False,default=None)
    Title=models.CharField(max_length=50)
    Description=models.CharField(max_length=50)
    Debit=models.DecimalField(max_digits=15,decimal_places=3,default=None)
    Credit=models.DecimalField(max_digits=15,decimal_places=3,default=None)
    Balance=models.IntegerField()
    Date_Of_Entry=models.DateField(format('YY-MM-DD'))
    Voucher_Flag=models.BooleanField(default=False)
    Current_Date_Time=models.DateTimeField(default=now)



    def __str__(self):
        return self.Elementary_Head_ID


class paymentOut(models.Model):
    Purchase_Contract_ID=models.ForeignKey('Purchase.contracts',on_delete=models.CASCADE,verbose_name='Purchase Contract')
    Account_ID=models.ForeignKey(elementaryhead,on_delete=models.CASCADE,editable=False)
    Cheque_No=models.IntegerField(verbose_name='Cheque No')
    Cheque_Img=models.ImageField(upload_to='assets/images/%Y/%m/%d',verbose_name='Cheque Image')
    Deposit_No=models.IntegerField(verbose_name='Deposit No')
    Deposit_Img=models.ImageField(upload_to='assets/images/%Y/%m/%d')
    Total_Units=models.IntegerField(verbose_name='Total Units')
    Date_Of_Entry=models.DateField(default=now)
    def __str__(self):
        return self.Account_ID


class paymentOutDetails(models.Model):
    Payment_Out_ID=models.ForeignKey(paymentOut,on_delete=models.CASCADE)
    No_Of_Bags=models.IntegerField()
    No_Of_Additional_Cones=models.IntegerField()



class paymentIn(models.Model):
    Sale_Contract_ID=models.ForeignKey('Purchase.contracts',on_delete=models.CASCADE,verbose_name='Sale Contract')
    Account_ID=models.ForeignKey(elementaryhead,on_delete=models.CASCADE,editable=False)
    Cheque_No=models.IntegerField(verbose_name='Cheque No')
    Cheque_Image=models.ImageField(upload_to='assets/images/%Y/%m/%d',verbose_name='Cheque Image')
    Deposit_No=models.IntegerField(verbose_name='Deposit No')
    Deposit_Image=models.ImageField(upload_to='assets/images/%Y/%m/%d')
    Total_Units=models.IntegerField(verbose_name='Total Units')
    Date_Of_entry=models.DateField(default=datetime.now)
    def __str__(self):
        return self.Account_ID


class paymentInDetails(models.Model):
    Payment_In_ID=models.ForeignKey(paymentOut,on_delete=models.CASCADE)
    No_Of_Bags=models.IntegerField()
    No_Of_Additional_Cones=models.IntegerField()





