from django.contrib import admin
from Inventory.models import counts,brands,productDetails,products,inventoryIn,productsPacking

# Register your models here.
admin.site.register(counts)
admin.site.register(brands)

class productDetailsAdmin(admin.ModelAdmin):
    fields=['Product_Name','Product_Label','Part_Number','Brand_ID','Count_ID','addInventory']

    class Media:
        js = ('js/main.js',)
    def save_model(self, request, obj, form, change):


        form.save()
        if request.POST.get('Starting_Units') and request.POST.get('Starting_Price'):
            startinginventory = int(request.POST.get('Starting_Units'))
            startingprice = int(request.POST.get('Starting_Price'))
            pdID=productDetails.objects.last()
            products.objects.create(Product_Details_ID=pdID,Starting_Units=startinginventory,Starting_Price=startingprice
                                ,Units_Received=0,Units_Shipped=0,Current_Units=startinginventory,Current_Price=startingprice,Minimum_Required=0)


class inventoryInAdmin(admin.ModelAdmin):
    fields = ['Purchase_Contract_ID','Units_In','Do_Type','Do_ID','Do_Image','Invoice_ID','Invoice_Image','Aging_Date','Lab_Report_Image','Payment_Days']

    class Media:
        js = ('js/addInventory.js',)






admin.site.register(inventoryIn,inventoryInAdmin)


admin.site.register(productDetails,productDetailsAdmin)
admin.site.register(products)

class productPackingAdmin(admin.ModelAdmin):
    readonly_fields = ('Weight_Per_Cone',)
    list_display = ['Name','Weight_Per_Bag','Cones_Per_Bag']

    class Media:
        js=('js/addInventory.js',)

admin.site.register(productsPacking,productPackingAdmin)
