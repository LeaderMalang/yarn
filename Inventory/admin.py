from django.contrib import admin
from Inventory.models import counts,brands,productDetails,products
# Register your models here.
admin.site.register(counts)
admin.site.register(brands)
admin.site.register(productDetails)
admin.site.register(products)
