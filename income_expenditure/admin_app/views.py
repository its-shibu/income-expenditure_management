from django.shortcuts import render

# Create your views here.
from .models import IncomeExpense

def dashboard(request):
    income = IncomeExpense.objects.filter(is_income=True)
    expenses = IncomeExpense.objects.filter(is_income=False)
    context = {
        'income': income,
        'expenses': expenses,
    }
    return render(request, 'mainpage.html', context)