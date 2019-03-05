"""YarnMMS URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path,include
from django.conf.urls import url
from Accounts import views as AC
from Accounts.views import *
from Inventory  import views as IN


urlpatterns = [
    path('admin/', admin.site.urls),
    url(r'^head/', AC.index, name='heads'),
    url(r'^subhead/', AC.subhead, name='subhead'),
    url(r'^elementaryhead/', AC.elementaryHead, name='elementaryhead'),
    url(r'^addacounts/', AC.addAccount, name='addacounts'),
    url(r'^loadsubhead/', AC.loadsubhead, name='loadsubhead'),
    url(r'^saveAccounts/', AC.saveAccounts, name='saveAccounts'),
    url(r'^journajVoucher/', AC.journajVoucher, name='journajVoucher'),
    url(r'^savejournalVoucher/', AC.savejournalVoucher, name='savejournalVoucher'),
    url(r'^accountBalances/', AC.accountBalance, name='accountBalances'),
    url(r'^restHead/$', CreateView.as_view(), name="create"),
    url(r'^restSubHead/$', CreateViewSubhead.as_view(), name="createsubhead"),
    url(r'^trialBalance/', AC.trialBalance, name="trialBalance"),
    url(r'^caltrialBalance/', AC.calTrailBalance, name="caltrialBalance"),
    url(r'^cpVoucher/', AC.cpVoucher, name="cpVoucher"),
    # url(r'^getContractDetail/', IN.getContractDetail, name="getContractDetail"),
]
