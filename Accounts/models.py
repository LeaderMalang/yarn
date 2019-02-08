from django.db import models
from django_countries.fields import CountryField
import datetime

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
    dateTime=models.DateTimeField(default=datetime.datetime.now())



    def __str__(self):
        return self.elementary




