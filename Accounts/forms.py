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