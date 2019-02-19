from django.contrib import admin
from Inventory.models import counts,brands,productDetails,products,AddInventory

# Register your models here.
admin.site.register(counts)
admin.site.register(brands)

class productDetailsAdmin(admin.ModelAdmin):
    fields=['name','label','partNumber','brand','count','addInventory']

    class Media:
        js = ('js/main.js',)
    def save_model(self, request, obj, form, change):
        startinginventory = int(request.POST.get('startinginventory'))
        startingprice = int(request.POST.get('startingprice'))
        form.save()
        pdID=productDetails.objects.last()
        products.objects.create(productDetailsID=pdID,startingInventory=startinginventory,startingPrice=startingprice
                                ,inventoryReceived=0,inventoryShipped=0,currentInventory=startinginventory,currentPrice=startingprice,minimumRequired=0)


class AddInventoryAdmin(admin.ModelAdmin):
    fields = ['purchaseContractID','unitsIn','doType','doID','doImage','invoiceID','invoiceImage','agingDate','labReportImage','enterPaymentDays']

    class Media:
        js = ('js/addInventory.js',)

    def save_model(self, request, obj, form, change):
        supplierID_id=int(request.get('supplierID_id'))
        form.save()




admin.site.register(AddInventory,AddInventoryAdmin)


admin.site.register(productDetails,productDetailsAdmin)
admin.site.register(products)
