from django.http import HttpResponse
from django.shortcuts import render

def homepage(request):
    return render(request,'home.html')

def businesspage(request):
    return render(request, 'business.html')

def commercialpage(request):
    return render(request, 'commercial.html')

def travelpage(request):
    return render(request, 'travel.html')

def educationcenterpage(request):
    return render(request, 'education_center.html')

def creditscorepage(request):
    return render(request, 'credit_score.html')

def financialgoals(request):
    return render(request, 'financial_goals.html')

def choosecheckingaccount(request):
    return render(request, 'choose_checking_account.html')

def debitcardforkids(request):
    return render(request, 'debit_card_for_kids.html')