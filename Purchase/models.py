from django.db import models
from django_countries.fields import CountryField


from Accounts.models import elementaryhead
from datetime import datetime
from django.utils.timezone import now
import base64

# Create your models here.
class suppliers(models.Model):
    Company_Name=models.CharField(max_length=30,verbose_name='Company Name',unique=True)
    Company_Address=models.CharField(max_length=50,verbose_name='Company Address')
    City=models.CharField(max_length=20,verbose_name='City')
    Region=models.CharField(max_length=20,verbose_name='Region')
    Country=CountryField()
    Postal_Code=models.IntegerField(verbose_name='Postal Code')
    Company_Phone=models.IntegerField(verbose_name="Company Phone")
    Company_Fax=models.IntegerField(verbose_name='Company Fax')
    Elementary_Head=models.ForeignKey(elementaryhead,on_delete=models.CASCADE,default=None,null=True,verbose_name='Elementary head',editable=False)
    Home_Page=models.URLField(default=None,verbose_name='Home Page')

    def save(self, force_insert=False, force_update=False, using=None,
             update_fields=None):
        accountID = elementaryhead.objects.order_by('id').last().id + 1
        code = '00003-000010-0000' + str(accountID)
        subhead=10
        elementaryhead.objects.create(subhead_id=subhead, name=self.Company_Name,Fixed_Flag=False, Account_Codes=code, Right=True)
        accountID = elementaryhead.objects.order_by('id').last().id + 1
        subhead=11
        code = '00003-000011-0000' + str(accountID)
        elementaryhead.objects.create(subhead_id=subhead, name=self.Company_Name+'(I/TAX PAYABLE)',Fixed_Flag=False, Account_Codes=code, Right=True)
        accountID = elementaryhead.objects.order_by('id').last().id + 1
        subhead=11
        code = '00003-000015-0000' + str(accountID)
        elementaryhead.objects.create(subhead_id=subhead, name=self.Company_Name+'(GST W/HELD PAYABLE)',Fixed_Flag=False, Account_Codes=code, Right=True)

        super(suppliers,self).save()

    def __str__(self):
        return self.Company_Name



class Contacts(models.Model):
    Supplier_ID=models.ForeignKey(suppliers,on_delete=models.CASCADE,verbose_name='Company')
    First_Name=models.CharField(max_length=35,verbose_name='First Name')
    Last_Name=models.CharField(max_length=35,verbose_name='Last Name')
    Suffix=models.CharField(max_length=10,verbose_name='Suffix')
    My_CHOICES=(('mr','MR'),('ms','MS'))
    Title=models.CharField(max_length=10,verbose_name='Title',choices=My_CHOICES)
    Phone_1=models.BigIntegerField(verbose_name='Phone')
    Phone_2=models.BigIntegerField(verbose_name='Another Phone',default=None)
    Mobile_1=models.BigIntegerField(verbose_name='Mobile',unique=True)
    Mobile_2=models.BigIntegerField(verbose_name='Another Mobile',default=None)
    Email=models.EmailField(unique=True)
    Fax=models.IntegerField(default=None,verbose_name='Fax')

    def __str__(self):
        return str(self.Supplier_ID)



class contracts(models.Model):
    Product_Detail_ID=models.ForeignKey('Inventory.productDetails',related_name='+',on_delete=models.CASCADE,verbose_name='Select Product',default=None)
    Supplier_ID=models.ForeignKey(suppliers,on_delete=models.CASCADE,verbose_name='Select Supplier',default=None)
    Total_Units=models.IntegerField(verbose_name='Total Units',editable=False,default=None)
    Sale_Tax=models.IntegerField(verbose_name='Sale Tax',default=None)
    Income_Tax=models.IntegerField(verbose_name='Income Tax',default=None)
    Sale_Tax_With_Held=models.IntegerField(verbose_name='Sale Tax with Held',default=None)
    Start_Date=models.DateField(verbose_name='Start Date',default=None)
    End_Date=models.DateField(verbose_name='End Date',default=None)
    Rate_Per_Unit = models.IntegerField(verbose_name='Rate Per Unit', default=None)
    Manul_Contract_Number=models.IntegerField(verbose_name='Manul Contract Number',default=None)
    Payment_Days=models.IntegerField(verbose_name='Payment Days',default=None)
    Remarks=models.CharField(verbose_name='Remarks',max_length=100,default=None)
    Date_Of_Entry=models.DateField(editable=False,default=now)
    Status=models.NullBooleanField(default=True,null=True,editable=False)
    def __str__(self):
        return str(self.Product_Detail_ID.name)





class contractDetails(models.Model):
    Purchase_Contract_ID=models.ForeignKey(contracts,on_delete=models.CASCADE,verbose_name='Select Contract')
    Product_Packing_ID=models.ForeignKey('Inventory.productsPacking',on_delete=models.CASCADE,verbose_name='Product Packing',null=True)
    No_Of_Bags=models.IntegerField(verbose_name='No of Bags')
    No_Of_Additional=models.IntegerField(verbose_name='No of Additional Cones')
    def __str__(self):
        return str(self.Purchase_Contract_ID)












