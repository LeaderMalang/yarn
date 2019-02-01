from django.shortcuts import render
from Accounts.models import heads,subheads,elementaryhead
from Accounts.forms import *
from django.http import JsonResponse
from django.core import serializers
from django.db.models import Sum
from Accounts.forms import *
from django.db import connection,transaction
from .serializers import *
from rest_framework import generics
import datetime
# Create your views here.

class CreateView(generics.ListCreateAPIView):
    """This class defines the create behavior of our rest api."""
    queryset = heads.objects.all()
    serializer_class = HeadsSerializer

    def perform_create(self, serializer):
        """Save the post data when creating a new bucketlist."""
        serializer.save()


class CreateViewSubhead(generics.ListCreateAPIView):
    """This class defines the create behavior of our rest api."""
    queryset = subheads.objects.all()
    serializer_class = SubHeadSerializer

    def perform_create(self, serializer):
        """Save the post data when creating a new bucketlist."""
        serializer.save()

def index(request):
    allhead=heads.objects.all()
    return  render(request, 'head.html',{'heads':allhead})


def subhead(request):
    assets=subheads.objects.filter(head=1)
    equity=subheads.objects.filter(head=4)
    liability=subheads.objects.filter(head=3)
    revenue=subheads.objects.filter(head=5)
    expense=subheads.objects.filter(head=2)

    return render(request,'subhead.html',{"assets":assets,"equity":equity,"liability":liability,"revenue":revenue,"expense":expense})


def elementaryHead (request):
    assetsQuery = elementaryhead.objects.raw('SELECT ele.name as elementaryHead,ele.id,sub.name as subHead FROM `Accounts_subheads` as sub JOIN Accounts_elementaryhead ele ON sub.head_id=1 AND ele.subhead_id=sub.id')
    equity = elementaryhead.objects.raw('SELECT ele.name as elementaryHead,ele.id,sub.name as subHead FROM `Accounts_subheads` as sub JOIN Accounts_elementaryhead ele ON sub.head_id=3 AND ele.subhead_id=sub.id')
    liability = elementaryhead.objects.raw('SELECT ele.name as elementaryHead,ele.id,sub.name as subHead FROM `Accounts_subheads` as sub JOIN Accounts_elementaryhead ele ON sub.head_id=2 AND ele.subhead_id=sub.id')
    revenue = elementaryhead.objects.raw('SELECT ele.name as elementaryHead,ele.id,sub.name as subHead FROM `Accounts_subheads` as sub JOIN Accounts_elementaryhead ele ON sub.head_id=5 AND ele.subhead_id=sub.id')
    expense = elementaryhead.objects.raw('SELECT ele.name as elementaryHead,ele.id,sub.name as subHead FROM `Accounts_subheads` as sub JOIN Accounts_elementaryhead ele ON sub.head_id=4 AND ele.subhead_id=sub.id')
    return render(request,'elementaryhead.html',{"assets":assetsQuery,"equity":equity,"liability":liability,"revenue":revenue,"expense":expense})

def addAccount(request):
    form=AccountsForm()
    form.fields['head'].choices=((0,'Select Head'),(1,'ASSETS'),(3,'LIABILITIES'),(4,'EQUITY'),(2,'EXPENSE'),(5,'REVENUE'))


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
        accountID = elementaryhead.objects.order_by('id').last().id + 1

        subheadID=request.POST.get('subhead')
        headID=request.POST.get('head')
        code = '0000'+str(headID)+'-'+ '0000' + str(subheadID) + '-0000' + str(accountID)
        if int(headID) in [1,2]:
            elementary = elementaryhead.objects.create(subhead=subheads.objects.get(id=subheadID),name=request.POST.get('name'), fixed=False, codes=code,left=True)
        elif int(headID) in [3,4,5]:
            elementary = elementaryhead.objects.create(subhead=subheads.objects.get(id=subheadID),
                                                       name=request.POST.get('name'), fixed=False, codes=code,
                                                       right=True)




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
        totaldebit=0
        totalcredit=0

        for i in range(int(totalelements)):
            balance = 0
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

            if debit:
                debit = float(debit)
                totaldebit=totaldebit+debit
            if credit:
                credit = float(credit)
                totalcredit=totalcredit+credit

            # print(amount, accountID, tID.id,debit,credit)

            accountID = int(accountID)
            accountType=elementaryhead.objects.values('left','right').filter(id=accountID)
            lastBalance=accounts.objects.values('balance').filter(elementary=accountID).last()
            left=accountType[0].get('left')
            right=accountType[0].get('right')

            if lastBalance:
                lastBalance = lastBalance.get('balance')

                if debit and left:
                    balance = lastBalance + debit
                elif debit:
                    balance = lastBalance-debit

                if credit and right:
                    balance=lastBalance+credit
                elif credit:
                    balance=lastBalance-credit
            else:
                if debit and left:
                     balance=balance+debit
                else:
                    balance=balance-debit
                if credit and right:
                    balance=balance+credit
                else:
                    balance=balance-credit



            query = ''' INSERT INTO `Accounts_accounts`(`voucherType`, `title`, `description`, `balance`, `date`, `voucherFlag`, `dateTime`, `elementary_id`, `voucherID_id`, `credit`, `debit`) VALUES
                                                     (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s) '''

            c = connection.cursor()
            try:
                c.execute(query, [voucherType, '', description,balance, date, 0, datetime.datetime.now(), accountID, voucherID.id,credit,debit])
            finally:
                c.close()

    return elementaryHead(request)

def accountBalance(request):
    balances=accounts.objects.aggregate(Sum('amount'))
    bal=accounts.objects.select_related('elementary')
    print(bal)
    return render(request,'test2.html')

def trialBalance(request):
    return render(request,'trialBalance.html')

def calTrailBalance(request):
    start=request.GET.get('start')
    end=request.GET.get('end')
    trialBalances=accounts.objects.raw("SELECT id,elementary_id,(SUM(debit)-SUM(credit)) As res FROM `Accounts_accounts` where date BETWEEN '"+start+"' and  '"+end+"' GROUP By elementary_id")
    dicttrailbalances=[]
    totaldebit=0
    totalcredit=0
    for trialBalance in trialBalances:
        acc=elementaryhead.objects.get(id=trialBalance.elementary_id)
        if trialBalance.res>0:
            totaldebit=totaldebit+trialBalance.res
            dicttrailbalances.append([acc,trialBalance.res,0])

        elif trialBalance.res<0:
            totalcredit=totalcredit+trialBalance.res
            dicttrailbalances.append([acc,0,trialBalance.res])
        print(acc,trialBalance.res)

    if not dicttrailbalances:
        raise ValueError("There is no Data for these dates")
    else:
        return render(request,'trialBalanceReport.html',{'trialbalances':dicttrailbalances,'totalDebit':totaldebit,'totalCredit':totalcredit})




