from django.contrib import admin
from Inventory.models import counts,brands,productDetails,products
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
        print(pdID)


admin.site.register(productDetails,productDetailsAdmin)
admin.site.register(products)
