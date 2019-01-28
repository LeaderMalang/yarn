from django.shortcuts import render
from Accounts.models import heads,subheads,elementaryhead
from Accounts.forms import *
from django.http import JsonResponse
from django.core import serializers
from django.db.models import Sum
from Accounts.forms import *
from django.db import connection,transaction
import datetime
# Create your views here.


def index(request):
    allhead=heads.objects.all()
    return  render(request, 'head.html',{'heads':allhead})


def subhead(request):
    assets=subheads.objects.filter(head=1)
    equity=subheads.objects.filter(head=3)
    liability=subheads.objects.filter(head=2)
    revenue=subheads.objects.filter(head=5)
    expense=subheads.objects.filter(head=4)

    return render(request,'subhead.html',{"assets":assets,"equity":equity,"liability":liability,"revenue":revenue,"expense":expense})


def elementaryHead (request):
    assets = elementaryhead.objects.filter(head=1).annotate(dcount=Sum('subhead_id'))
    equity = elementaryhead.objects.filter(head=3)
    liability = elementaryhead.objects.filter(head=2)
    revenue = elementaryhead.objects.filter(head=5)
    expense = elementaryhead.objects.filter(head=4)
    return render(request,'elementaryhead.html',{"assets":assets,"equity":equity,"liability":liability,"revenue":revenue,"expense":expense})

def addAccount(request):
    form=AccountsForm()
    return render(request,'addAccounts.html',{'form':form})

def loadsubhead(request):
    if request.method == 'POST':
        id=request.POST.get('id')
        subhead=subheads.objects.filter(head=id)
    data = {
        'subheads': serializers.serialize('json', subhead)
    }

    return JsonResponse(data,content_type="application/json")

def saveAccounts(request):
    if request.method == 'POST':
        elementary=AccountsForm(request.POST)
        if elementary.is_valid():
            newelementary=elementary.save(commit=False)
            accountID = elementaryhead.objects.order_by('id').last().id + 1
            headID=elementary.cleaned_data['head']
            subheadID=elementary.cleaned_data['subhead']
            newelementary.code = '0000'+str(headID.id)+'-'+ '0000' + str(subheadID.id) + '-0000' + str(accountID)
            newelementary.fixed=True
            newelementary.save()


    return elementaryHead(request)

def journajVoucher(request):
    form=TransactionItemFormset()
    return render(request,'journalVoucher.html',{'form':form})

def savejournalVoucher(request):
    if request.method == 'POST':
        journalVoucher=TransactionItemFormset(request.POST)

        vouchers = voucher()
        vouchers.save()
        voucherID = voucher.objects.latest('id')
        voucherType = "Journal"
        date = request.POST['form-1-date']
        totalelements = request.POST['tElements']
        for i in range(int(totalelements)):
            target = "form-" + str(i) + "-elementary"
            debitName = "form-" + str(i) + "-debit"
            creditName = "form-" + str(i) + "-credit"
            descriptionName = "form-" + str(i) + "-description"
            accountID = request.POST.get(target)
            if debitName in request.POST:
                debit = request.POST.get(debitName)
            else:
                debit = 0
            if creditName in request.POST:
                credit = request.POST.get(creditName)
            else:
                credit = 0
            description = request.POST.get(descriptionName)
            amount = 0
            if debit:
                amount = float(debit)
            if credit:
                amount = -float(credit)

            # print(amount, accountID, tID.id,debit,credit)

            accountID = int(accountID)
            head=elementaryhead.objects.values('head_id').get(id=accountID)
            subhead=elementaryhead.objects.values('subhead_id').get(id=accountID)
            query = ''' INSERT INTO `Accounts_accounts`(`voucherType`, `title`, `description`, `amount`, `balance`, `date`, `voucherFlag`, `dateTime`, `elementary_id`, `head_id`, `subhead_id`, `voucherID_id`) VALUES
                                                     (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s) '''
            c = connection.cursor()
            try:
                c.execute(query, [voucherType, '', description, amount, 0, date, 0, datetime.datetime.now(), accountID, head['head_id'],subhead['subhead_id'], voucherID.id])
            finally:
                c.close()

    return render(request,'test2.html')

def accountBalance(request):
    balances=accounts.objects.aggregate(Sum('amount'))
    bal=accounts.objects.select_related('elementary')
    print(bal)
    return render(request,'test2.html')




