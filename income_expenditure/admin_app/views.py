from django.shortcuts import render, redirect
from .models import *
from django.contrib import messages
from . forms import *



def frontpage(request):
    return render(request, 'frontpage.html',)




def dashboard(request):
    incomeData = IncomeDetails.objects.all()
    expensesData = ExpenditureDetails.objects.all()
    context = {
        'income': incomeData,
        'expenses': expensesData
    }
    return render(request, 'mainpage.html', context)



def addIncome(request):
    if request.method == 'POST':
        form = IncomForm(request.POST)
        if form.is_valid():
            form.save()
            messages.add_message(request, messages.SUCCESS, 'Income Details Added Successfully')
            return redirect('/addincome')
        else:
            messages.add_message(request, messages.ERROR, 'Failed to Add Details')
            return render(request, 'mainpage.html', {'form': form})

    context = {'form': IncomForm}
    return render(request, 'incomedetails.html', context)

def addExpenditure(request):
    if request.method == 'POST':
        form = ExpenditureForm(request.POST)
        if form.is_valid():
            form.save()
            messages.add_message(request, messages.SUCCESS, 'Expenditure Details Added Successfully')
            return redirect('/addexpenditure')
        else:
            messages.add_message(request, messages.ERROR, 'Failed to Add Details')
            return render(request, 'expendituredetails.html', {'form': form})
    context = {
        'form': ExpenditureForm
    }
    return render(request, 'expendituredetails.html', context)