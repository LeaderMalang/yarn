from django.db import models
from Purchase.models import *

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

    def save(self, force_insert=False, force_update=False, using=None,
             update_fields=None):
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