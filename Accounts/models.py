from django.db import models

# Create your models here.

class heads(models.Model):
    name = models.CharField(max_length=10)
    def __str__(self):
        return self.name


class subheads(models.Model):
    head=models.ForeignKey(heads,on_delete=models.CASCADE)
    name=models.CharField(max_length=30)
    def __str__(self):
        return self.name

class elementaryhead(models.Model):
    head=models.ForeignKey(heads,on_delete=models.CASCADE)
    subhead=models.ForeignKey(subheads,on_delete=models.CASCADE)
    name=models.CharField(max_length=50)
    code=models.CharField(max_length=50,editable=False,default=None)

    def __str__(self):
        return self.name

class voucher(models.Model):
    name=models.CharField(max_length=20)

    def __str__(self):
        return self.name

class accounts(models.Model):
    voucherID=models.ForeignKey(voucher,on_delete=models.CASCADE)
    head=models.ForeignKey(heads,on_delete=models.CASCADE)
    subhead=models.ForeignKey(subheads,on_delete=models.CASCADE)
    elementary=models.ForeignKey(elementaryhead,on_delete=models.CASCADE)
    voucherType=models.CharField(max_length=20,editable=False,default=None)
    title=models.CharField(max_length=50)
    description=models.CharField(max_length=50)
    amount=models.IntegerField(max_length=20)
    balance=models.IntegerField(max_length=20)
    date=models.DateField(format('YY-MM-DD'))
    voucherFlag=models.BooleanField(default=False)
    dateTime=models.DateTimeField()

    def __str__(self):
        return self.elementary


