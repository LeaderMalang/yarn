from django.db import models
from django_countries.fields import CountryField
from Accounts.models import elementaryhead
from Inventory.models import productDetails
from datetime import datetime

# Create your models here.
class suppliers(models.Model):
    companyName=models.CharField(max_length=30,verbose_name='Company Name')
    companyAddress=models.CharField(max_length=50,verbose_name='Company Address')
    city=models.CharField(max_length=20,verbose_name='City')
    region=models.CharField(max_length=20,verbose_name='Region')
    country=CountryField()
    postalCode=models.IntegerField(verbose_name='Postal Code')
    companyPhone=models.IntegerField(verbose_name="Company Phone")
    companyFax=models.IntegerField(verbose_name='Company Fax')
    elementaryID=models.ForeignKey(elementaryhead,on_delete=models.CASCADE,default=None,null=True,verbose_name='Elementary head',editable=False)
    buyer=models.BooleanField(default=None,verbose_name='Is Buyer',editable=False)
    supplier=models.BooleanField(default=None,verbose_name='Is Supplier',editable=False)
    website=models.URLField(default=None,verbose_name='Website')

    def save(self, force_insert=False, force_update=False, using=None,
             update_fields=None):
        accountID = elementaryhead.objects.order_by('id').last().id + 1
        code = '00003-000010-0000' + str(accountID)
        subhead=10
        elementaryhead.objects.create(subhead_id=subhead, name=self.companyName,fixed=False, codes=code, right=True)
        accountID = elementaryhead.objects.order_by('id').last().id + 1
        subhead=11
        code = '00003-000011-0000' + str(accountID)
        elementaryhead.objects.create(subhead_id=subhead, name=self.companyName+'(I/TAX PAYABLE)',fixed=False, codes=code, right=True)
        accountID = elementaryhead.objects.order_by('id').last().id + 1
        subhead=15
        code = '00003-000015-0000' + str(accountID)
        elementaryhead.objects.create(subhead_id=subhead, name=self.companyName+'(GST W/HELD PAYABLE)',fixed=False, codes=code, right=True)
        self.supplier = True
        self.buyer = False
        super(suppliers,self).save()

    def __str__(self):
        return self.companyName



class Contacts(models.Model):
    supplierID=models.ForeignKey(suppliers,on_delete=models.CASCADE,verbose_name='Company')
    firstName=models.CharField(max_length=35,verbose_name='First Name')
    lastName=models.CharField(max_length=35,verbose_name='Last Name')
    suffix=models.CharField(max_length=10,verbose_name='Suffix')
    My_CHOICES=(('mr','MR'),('ms','MS'))
    title=models.CharField(max_length=10,verbose_name='Title',choices=My_CHOICES)
    phone1=models.BigIntegerField(verbose_name='Phone')
    phone2=models.BigIntegerField(verbose_name='Another Phone',default=None)
    mobile1=models.BigIntegerField(verbose_name='Mobile')
    mobile2=models.BigIntegerField(verbose_name='Another Mobile',default=None)
    email=models.EmailField()
    fax=models.IntegerField(default=None,verbose_name='Fax')

    def __str__(self):
        return self.supplierID



class contracts(models.Model):
    productDetailID=models.ForeignKey(productDetails,on_delete=models.CASCADE,verbose_name='Select Product',default=None)
    supplierID=models.ForeignKey(suppliers,on_delete=models.CASCADE,verbose_name='Select Supplier',default=None)
    totalUnits=models.IntegerField(verbose_name='Total Units',editable=False,default=None)
    ratePerUnit=models.IntegerField(verbose_name='Rate Per Unit',default=None)
    saleTax=models.IntegerField(verbose_name='Sale Tax',default=None)
    incomeTax=models.IntegerField(verbose_name='Income Tax',default=None)
    saleTaxwithHeld=models.IntegerField(verbose_name='Sale Tax with Held',default=None)
    startDate=models.DateField(verbose_name='Start Date',default=None)
    endDate=models.DateField(verbose_name='End Date',default=None)
    manulContractNumber=models.IntegerField(verbose_name='Manul Contract Number',default=None)
    paymentDays=models.IntegerField(verbose_name='Payment Days',default=None)
    remarks=models.CharField(verbose_name='Remarks',max_length=100,default=None)
    dateOfEntry=models.DateField(editable=False,default=datetime.now())




class contractDetails(models.Model):
    contractID=models.ForeignKey(contracts,on_delete=models.CASCADE,verbose_name='Select Contract')
    weightPerBag=models.IntegerField(verbose_name='Weight Per Bag')
    conesPerBag=models.IntegerField(verbose_name='Cones Per Bag')
    weightPerCone=models.IntegerField(verbose_name='Weight Per Cone')
    noOfBags=models.IntegerField(verbose_name='No of Bags')
    noOfAdditional=models.IntegerField(verbose_name='No of Additional Cones')



