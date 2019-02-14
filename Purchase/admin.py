from django.contrib import admin
from Purchase.models import suppliers,Contacts,contracts,contractDetails






admin.site.register(suppliers)
admin.site.register(Contacts)


class contractDetailsInline(admin.TabularInline):
    model = contractDetails
    extra = 1
    fields = ["weightPerBag", "conesPerBag", "weightPerCone", 'noOfBags','noOfAdditional']

class contractsAdmin(admin.ModelAdmin):
    save_on_top = True
    fields = ["productDetailID",'supplierID','saleTax','incomeTax','ratePerUnit','saleTaxwithHeld','startDate','endDate','manulContractNumber','paymentDays','remarks']
    inlines = [contractDetailsInline,]

    def save_model(self, request, obj, form, change):
        noOfBags=int(request.POST.get('contractdetails_set-0-noOfBags'))
        weightPerBag=int(request.POST.get('contractdetails_set-0-weightPerBag'))
        conesPerBag=int(request.POST.get('contractdetails_set-0-conesPerBag'))
        weightPerCone=int(request.POST.get('contractdetails_set-0-weightPerCone'))

        form.instance.totalUnits=(noOfBags * weightPerBag) + (conesPerBag * weightPerCone)

        form.save()
# Register your models here.


admin.site.register(contracts,contractsAdmin)




