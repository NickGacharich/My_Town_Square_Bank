"""
URL configuration for my_town_square_bank project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
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
from django.urls import include, path

from . import index 

urlpatterns = [
    path('', include('bank.urls')),
    path('business/', index.businesspage, name='business'),
    path('commercial/', index.commercialpage, name='commercial'),
    path('travel/', index.travelpage, name="travel"),
    path('education_center/',index.educationcenterpage, name="education_center"),
    path('credit_score/',index.creditscorepage, name="credit_score"),
    path('financial_goals/',index.financialgoals, name="financial_goals"),
    path('choose_checking_account/',index.choosecheckingaccount, name="choose_checking_account"),
    path('debit_card_for_kids/',index.debitcardforkids, name="debit_card_for_kids"),
    path('admin/', admin.site.urls),
]
