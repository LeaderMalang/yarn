from django import forms

from Accounts.models import *
from django.forms import formset_factory

class AccountsForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super(AccountsForm, self).__init__(*args, **kwargs)
        self.fields['head'].widget.attrs['class'] = 'form-control'
        self.fields['subhead'].widget.attrs['class'] = 'form-control'
        self.fields['name'].widget.attrs['class'] = 'form-control'

    class Meta:
        model=elementaryhead
        fields=('head','subhead','name',)

class trasactionForm(forms.ModelForm):
    debit=forms.DecimalField(max_digits=10,decimal_places=2)
    credit=forms.DecimalField(max_digits=10,decimal_places=2)


    def __init__(self, *args, **kwargs):
        super(trasactionForm, self).__init__(*args, **kwargs)
        self.fields['date'].widget.attrs['class'] = 'form-control'
        self.fields['elementary'].widget.attrs['class'] = 'form-control'
        self.fields['description'].widget.attrs['class'] = 'form-control'
        self.fields['amount'].widget.attrs['class'] = 'form-control'
        self.fields['debit'].widget.attrs['class'] = 'form-control'
        self.fields['credit'].widget.attrs['class'] = 'form-control'
    class Meta:
        model=accounts
        fields=('date','elementary','description','amount','debit','credit',)
        labels = {
            'Date', 'Elementary Head','Description','Amount','Debit','Credit'
        }

TransactionItemFormset = formset_factory(trasactionForm, extra=2)