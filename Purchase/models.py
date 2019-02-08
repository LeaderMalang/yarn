from django.db import models
from django_countries.fields import CountryField
from Accounts.models import elementaryhead

# Create your models here.
class users(models.Model):
    companyName=models.CharField(max_length=30,verbose_name='Company Name')
    contactPersonName=models.CharField(max_length=30,verbose_name='Contact Person Name')
    companyAddress=models.CharField(max_length=50,verbose_name='Company Address')
    city=models.CharField(max_length=20,verbose_name='City')
    region=models.CharField(max_length=20,verbose_name='Region')
    country=CountryField()
    postalCode=models.IntegerField(verbose_name='Postal Code')
    companyPhone=models.IntegerField(verbose_name="Company Phone")
    companyFax=models.IntegerField(verbose_name='Company Fax')
    elementaryID=models.ForeignKey(elementaryhead,on_delete=models.CASCADE,default=None,null=True,verbose_name='Elementary head',editable=False)
    buyer=models.BooleanField(default=False,verbose_name='Is Buyer')
    supplier=models.BooleanField(default=False,verbose_name='Is Supplier')

    def save(self, force_insert=False, force_update=False, using=None,
             update_fields=None):

        if self.supplier:
            accountID = elementaryhead.objects.order_by('id').last().id + 1
            code = '00003-000010-0000' + str(accountID)
            subhead=10
            ele=elementaryhead.objects.create(subhead_id=subhead, name=self.companyName,
                                      fixed=False, codes=code, right=True)
        elif self.buyer:
            accountID = elementaryhead.objects.order_by('id').last().id + 1
            code = '00001-00004-0000' + str(accountID)
            subhead = 4
            ele=elementaryhead.objects.create(subhead_id=subhead, name=self.companyName,
                                          fixed=False, codes=code, left=True)
        self.elementaryID=ele


        super(users,self).save()

    def __str__(self):
        return self.companyName

class counts(models.Model):
    name=models.CharField(max_length=30)

    def __str__(self):
        return self.name


class brands(models.Model):
    name=models.CharField(max_length=30)

    def __str__(self):
        return self.name