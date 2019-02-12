from django.db import models
from Purchase.models import users
from Accounts.models import *
# Create your models here.

class customers(users):

    def save(self, force_insert=False, force_update=False, using=None,
             update_fields=None):
        accountID = elementaryhead.objects.order_by('id').last().id + 1
        code = '00001-000010-0000' + str(accountID)
        subhead=10
        elementaryhead.objects.create(subhead_id=subhead, name=self.companyName,fixed=False, codes=code, right=True)
        accountID = elementaryhead.objects.order_by('id').last().id + 1
        subhead=11
        code = '00001-000011-0000' + str(accountID)
        elementaryhead.objects.create(subhead_id=subhead, name=self.companyName+'(I/TAX PAYABLE)',fixed=False, codes=code, right=True)
        accountID = elementaryhead.objects.order_by('id').last().id + 1
        subhead=15
        code = '00001-000015-0000' + str(accountID)
        elementaryhead.objects.create(subhead_id=subhead, name=self.companyName+'(GST W/HELD PAYABLE)',fixed=False, codes=code, right=True)
        self.supplier = True
        self.buyer = False
        super(users,self).save()