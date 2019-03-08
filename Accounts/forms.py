from django import forms

from Accounts.models import *
from django.forms import formset_factory

class AccountsForm(forms.ModelForm):

    head=forms.ChoiceField()
    def __init__(self, *args, **kwargs):
        super(AccountsForm, self).__init__(*args, **kwargs)
        self.fields['head'].widget.attrs['class'] = 'form-control'
        self.fields['Subhead_ID'].widget.attrs['class'] = 'form-control'
        self.fields['Name'].widget.attrs['class'] = 'form-control'

    class Meta:
        model=elementaryhead
        fields=('head','Subhead_ID','Name')

class trasactionForm(forms.ModelForm):

    def __init__(self, *args, **kwargs):
        super(trasactionForm, self).__init__(*args, **kwargs)
        self.fields['Date_Of_Entry'].widget.attrs['class'] = 'form-control'
        self.fields['Elementary_Head_ID'].widget.attrs['class'] = 'form-control'
        self.fields['Description'].widget.attrs['class'] = 'form-control'
        self.fields['Debit'].widget.attrs['class'] = 'form-control'
        self.fields['Credit'].widget.attrs['class'] = 'form-control'
    class Meta:
        model=accounts
        fields=('Date_Of_Entry','Elementary_Head_ID','Description','Debit','Credit',)
        # labels = {
        #     'Date', 'Elementary Head','Description','Debit','Credit'
        # }

TransactionItemFormset = formset_factory(trasactionForm, extra=2)