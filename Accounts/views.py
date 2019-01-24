from django.shortcuts import render
from Accounts.models import heads,subheads,elementaryhead
from Accounts.forms import *
from django.http import JsonResponse
from django.core import serializers
from django.db.models import Count,Sum
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
            newelementary.save()


    return elementaryHead(request)


