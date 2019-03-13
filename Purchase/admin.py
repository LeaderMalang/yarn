from django.contrib import admin
from Purchase.models import suppliers,Contacts,contracts,contractDetails
from Inventory.models import productsPacking






admin.site.register(suppliers)
admin.site.register(Contacts)


class contractDetailsInline(admin.TabularInline):
    model = contractDetails
    extra = 1
    fields = ["productPackingID", "noOfBags", "noOfAdditional"]

class contractsAdmin(admin.ModelAdmin):
    save_on_top = True
    fields = ["productDetailID",'supplierID','saleTax','incomeTax','ratePerUnit','saleTaxwithHeld','startDate','endDate','manulContractNumber','paymentDays','remarks']
    inlines = [contractDetailsInline,]
    class Media:
        js = ('js/addInventory.js',)

    def save_model(self, request, obj, form, change):
        productPackingID=int(request.POST.get('contractdetails_set-0-productPackingID'))
        noOfBags=int(request.POST.get('contractdetails_set-0-noOfBags'))
        noOfadd=int(request.POST.get('contractdetails_set-0-noOfAdditional'))
        productPackingRecord=productsPacking.objects.values('weightPerBag','conesPerBag','weightPerCone').filter(id=productPackingID)
        print(productPackingRecord[0].get('weightPerBag'))

        form.instance.totalUnits=(noOfBags * productPackingRecord[0].get('weightPerBag')) + (noOfadd * productPackingRecord[0].get('weightPerCone'))

        form.save()
# Register your models here.


admin.site.register(contracts,contractsAdmin)




