from django.shortcuts import render
from django.http import JsonResponse
from django.core import serializers
from Purchase.models import contractDetails

# Create your views here.

def getContractDetail(request):
    if request.method== 'POST':
        contractID=request.POST.get('contractID')
        contractDetail=contractDetails.objects.values('weightPerBag','conesPerBag','weightPerCone','noOfBags','noOfAdditional').filter(contractID=contractID)

        data = {
            'contractDetails':  contractDetail[0]
        }

    return JsonResponse(data, content_type="application/json")

