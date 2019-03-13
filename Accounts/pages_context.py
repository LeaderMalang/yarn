from .models import accounts
from Inventory.models import productDetails,productsPacking
from Purchase.models import suppliers,Contacts,contracts

def show_pages_menu(context):


    pages_menu= suppliers.objects.filter(show_in_menu=True)

    return {'pages_menu': pages_menu}