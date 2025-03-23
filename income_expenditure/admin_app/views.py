from django.shortcuts import render

# Create your views here.
from .models import *
from . forms import *



def frontpage(request):
    return render(request, 'frontpage.html',)

def dashboard(request):
    income = IncomeExpense.objects.filter(is_income=True)
    expenses = IncomeExpense.objects.filter(is_income=False)
    context = {
        'income': income,
        'expenses': expenses,
    }
    return render(request, 'mainpage.html', context)


def addIncome(request):
    context = {'form': IncomForm}
    return render(request, 'incomedetails.html', context)


def addExpenditure(request):
    context = {'form': ExpenditureForm}
    return render(request, 'expendituredetails.html', context)
