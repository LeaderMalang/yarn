from django.contrib import admin
from Purchase.models import suppliers,Contacts,contracts,contractDetails
from Inventory.models import productsPacking






admin.site.register(suppliers)
admin.site.register(Contacts)


class contractDetailsInline(admin.TabularInline):
    model = contractDetails
    extra = 1
    fields = ["Product_Packing_ID", "No_Of_Bags", "No_Of_Additional"]

class contractsAdmin(admin.ModelAdmin):
    save_on_top = True
    fields = ["Product_Detail_ID",'Supplier_ID','Sale_Tax','Income_Tax','Rate_Per_Unit','Sale_Tax_With_Held','Start_Date','End_Date','Manul_Contract_Number','Payment_Days','Remarks']
    inlines = [contractDetailsInline,]
    class Media:
        js = ('js/addInventory.js',)

    def save_model(self, request, obj, form, change):
        productPackingID=int(request.POST.get('contractdetails_set-0-Product_Packing_ID'))
        noOfBags=int(request.POST.get('contractdetails_set-0-No_Of_Bags'))
        noOfadd=int(request.POST.get('contractdetails_set-0-No_Of_Additional'))
        productPackingRecord=productsPacking.objects.values('weightPerBag','conesPerBag','weightPerCone').filter(id=productPackingID)
        print(productPackingRecord[0].get('weightPerBag'))

        form.instance.totalUnits=(noOfBags * productPackingRecord[0].get('weightPerBag')) + (noOfadd * productPackingRecord[0].get('weightPerCone'))

        form.save()
# Register your models here.


admin.site.register(contracts,contractsAdmin)




