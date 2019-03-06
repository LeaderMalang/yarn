from django.contrib import admin
from Inventory.models import counts,brands,productDetails,products,inventoryIn,productsPacking

# Register your models here.
admin.site.register(counts)
admin.site.register(brands)

class productDetailsAdmin(admin.ModelAdmin):
    fields=['name','label','partNumber','brand','count','addInventory']

    class Media:
        js = ('js/main.js',)
    def save_model(self, request, obj, form, change):


        form.save()
        if request.POST.get('startinginventory') and request.POST.get('startingprice'):
            startinginventory = int(request.POST.get('startinginventory'))
            startingprice = int(request.POST.get('startingprice'))
            pdID=productDetails.objects.last()
            products.objects.create(productDetailsID=pdID,startingInventory=startinginventory,startingPrice=startingprice
                                ,inventoryReceived=0,inventoryShipped=0,currentInventory=startinginventory,currentPrice=startingprice,minimumRequired=0)


class inventoryInAdmin(admin.ModelAdmin):
    fields = ['purchaseContractID','unitsIn','doType','doID','doImage','invoiceID','invoiceImage','agingDate','labReportImage','enterPaymentDays']

    class Media:
        js = ('js/addInventory.js',)






admin.site.register(inventoryIn,inventoryInAdmin)


admin.site.register(productDetails,productDetailsAdmin)
admin.site.register(products)

class productPackingAdmin(admin.ModelAdmin):
    readonly_fields = ('weightPerCone',)
    list_display = ['name','weightPerBag','conesPerBag']

    class Media:
        js=('js/addInventory.js',)

admin.site.register(productsPacking,productPackingAdmin)
