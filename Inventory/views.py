from django.http import JsonResponse
from Inventory.models import productsPacking
from Purchase.models import contracts,contractDetails



# Create your views here.

def getProductPackingDetail(request):
    if request.method== 'POST':
        productPackingID=request.POST.get('productPackingID')
        packingRecord=productsPacking.objects.values('weightPerBag','conesPerBag','weightPerCone').filter(id=productPackingID)

        data = {
            'packingRecord':  packingRecord[0]
        }

    return JsonResponse(data, content_type="application/json")

def getContractDetail(request):
    if request.method== 'POST':
        contractID=request.POST.get('purchaseContractID')
        contractRecord=contractDetails.objects.values('noOfBags','noOfAdditional','productPackingID').filter(contractID=contractID)
        productsPackingId=contractRecord[0].get('productPackingID')
        productPackingRecord=productsPacking.objects.values('name','weightPerBag','conesPerBag','weightPerCone').filter(id=productsPackingId)
        data = {
            'contractRecord':  contractRecord[0],
            'productPackingRecord':productPackingRecord[0]
        }

    return JsonResponse(data, content_type="application/json")

