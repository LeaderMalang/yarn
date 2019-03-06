from django.http import JsonResponse
from Inventory.models import productsPacking



# Create your views here.

def getProductPackingDetail(request):
    if request.method== 'POST':
        productPackingID=request.POST.get('productPackingID')
        packingRecord=productsPacking.objects.values('weightPerBag','conesPerBag','weightPerCone').filter(id=productPackingID)

        data = {
            'packingRecord':  packingRecord[0]
        }

    return JsonResponse(data, content_type="application/json")

