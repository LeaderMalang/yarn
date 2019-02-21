from django.shortcuts import render
from django.http import JsonResponse
from django.core import serializers
from Purchase.models import contractDetails,contracts
from Inventory.models import inventoryIn
from django.db.models import Sum

# Create your views here.

def getContractDetail(request):
    if request.method== 'POST':
        contractID=request.POST.get('purchaseContractID')
        contractDetail=contractDetails.objects.values('weightPerBag','conesPerBag','weightPerCone','noOfBags','noOfAdditional').filter(contractID=contractID)

        remainingBagRes=inventoryIn.objects.values('unitsIn').filter(purchaseContractID=contractID).aggregate(Sum('unitsIn'))
        if remainingBagRes:
            print(remainingBagRes)
            remainingBag=remainingBagRes.get('unitsIn__sum')
        else:
            remainingBag=0

        data = {
            'contractDetails':  contractDetail[0],
            'remainingBags':remainingBag
        }

    return JsonResponse(data, content_type="application/json")

