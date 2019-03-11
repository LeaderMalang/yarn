from django.shortcuts import render
from Accounts.models import heads,subheads,elementaryhead
from Accounts.forms import *
from django.http import JsonResponse
from django.http import HttpResponse
from django.db.models import Sum
from Accounts.forms import *
from django.db import connection,transaction
from .serializers import *
from rest_framework import generics
import datetime
import json



# Rest API List and Save EndPoints for Head
class CreateView(generics.ListCreateAPIView):
    """This class defines the create behavior of our rest api."""
    queryset = heads.objects.all()
    serializer_class = HeadsSerializer

    def perform_create(self, serializer):
        """Save the post data when creating a new bucketlist."""
        serializer.save()

# Rest API List and Save EndPoints for Sub Head
class CreateViewSubhead(generics.ListCreateAPIView):
    """This class defines the create behavior of our rest api."""
    queryset = subheads.objects.all()
    serializer_class = SubHeadSerializer

    def perform_create(self, serializer):
        """Save the post data when creating a new bucketlist."""
        serializer.save()
#  List view  for Head
def index(request):
    allhead=heads.objects.all()
    return  render(request, 'head.html',{'heads':allhead})

#List View for SubHead
def subhead(request):
    assets=subheads.objects.filter(Head_ID=1)
    equity=subheads.objects.filter(Head_ID=4)
    liability=subheads.objects.filter(Head_ID=3)
    revenue=subheads.objects.filter(Head_ID=5)
    expense=subheads.objects.filter(Head_ID=2)

    return render(request,'subhead.html',{"assets":assets,"equity":equity,"liability":liability,"revenue":revenue,"expense":expense})


def elementaryHead (request):
    assetsQuery = elementaryhead.objects.raw('SELECT ele.Name as elementaryHead,ele.id,sub.Name as subHead FROM `Accounts_subheads` as sub JOIN Accounts_elementaryhead ele ON sub.Head_ID_id=1 AND ele.Subhead_ID_id=sub.id')
    equity = elementaryhead.objects.raw('SELECT ele.Name as elementaryHead,ele.id,sub.Name as subHead FROM `Accounts_subheads` as sub JOIN Accounts_elementaryhead ele ON sub.Head_ID_id=3 AND ele.Subhead_ID_id=sub.id')
    liability = elementaryhead.objects.raw('SELECT ele.Name as elementaryHead,ele.id,sub.Name as subHead FROM `Accounts_subheads` as sub JOIN Accounts_elementaryhead ele ON sub.Head_ID_id=2 AND ele.Subhead_ID_id=sub.id')
    revenue = elementaryhead.objects.raw('SELECT ele.Name as elementaryHead,ele.id,sub.Name as subHead FROM `Accounts_subheads` as sub JOIN Accounts_elementaryhead ele ON sub.Head_ID_id=5 AND ele.Subhead_ID_id=sub.id')
    expense = elementaryhead.objects.raw('SELECT ele.Name as elementaryHead,ele.id,sub.Name as subHead FROM `Accounts_subheads` as sub JOIN Accounts_elementaryhead ele ON sub.Head_ID_id=4 AND ele.Subhead_ID_id=sub.id')
    return render(request,'elementaryhead.html',{"assets":assetsQuery,"equity":equity,"liability":liability,"revenue":revenue,"expense":expense})

def addAccount(request):
    form=AccountsForm()
    form.fields['head'].choices=((0,'Select Head'),(1,'ASSETS'),(3,'LIABILITIES'),(4,'EQUITY'),(2,'EXPENSE'),(5,'REVENUE'))


    return render(request,'addAccounts.html',{'form':form})

def loadsubhead(request):
    if request.method == 'POST':
        id=request.POST.get('id')
        subhead=subheads.objects.values().filter(Head_ID=id)


    subhead=json.dumps(list(subhead))
    #data =serializers.serialize('json',subhead)
    response=HttpResponse(subhead,content_type="application/json")

    return response

def saveAccounts(request):
    if request.method == 'POST':
        accountID = elementaryhead.objects.order_by('id').last().id + 1

        subheadID=request.POST.get('Subhead_ID')
        headID=request.POST.get('Head_ID')
        code = '0000'+str(headID)+'-'+ '0000' + str(subheadID) + '-0000' + str(accountID)
        if int(headID) in [1,2]:
            elementary = elementaryhead.objects.create(Subhead_ID=subheads.objects.get(id=subheadID),Name=request.POST.get('name'), Fixed_Flag=False, Account_Codes=code,Left=True)
        elif int(headID) in [3,4,5]:
            elementary = elementaryhead.objects.create(Subhead_ID=subheads.objects.get(id=subheadID),
                                                       Name=request.POST.get('name'), Fixed_Flag=False, Account_Codes=code,
                                                       Right=True)




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
            target = "form-" + str(i) + "-Elementary_Head_ID"
            debitName = "form-" + str(i) + "-Debit"
            creditName = "form-" + str(i) + "-Credit"
            descriptionName = "form-" + str(i) + "-Description"
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
            lastBalance=accounts.objects.values('balance').filter(Elementary_Head_ID=accountID).last()
            left=accountType[0].get('left')
            right=accountType[0].get('right')

            if lastBalance:
                lastBalance = lastBalance.get('Balance')

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



            query = ''' INSERT INTO `Accounts_accounts`(`Voucher_Type`, `Title`, `Description`, `Balance`, `Date_Of_Entry`, `Voucher_Flag`, `Current_Date_Time`, `Elementary_Head_ID`, `Voucher_ID`, `Credit`, `Debit`) VALUES
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
    trialBalances=accounts.objects.raw("SELECT id,Elementary_Head_ID,(SUM(Debit)-SUM(Credit)) As res FROM `Accounts_accounts` where date BETWEEN '"+start+"' and  '"+end+"' GROUP By Elementary_Head_ID")
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

    if not dicttrailbalances:
        raise ValueError("There is no Data for these dates")
    else:
        return render(request,'trialBalanceReport.html',{'trialbalances':dicttrailbalances,'totalDebit':totaldebit,'totalCredit':totalcredit})


def cpVoucher(request):
    form = TransactionItemFormset()
    return  render(request,'cpVoucher.html',{'form':form})

