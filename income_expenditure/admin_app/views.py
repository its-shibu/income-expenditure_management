from django.shortcuts import render, redirect
from .models import *
from django.contrib import messages
from . forms import *
from django.db.models import Sum


def frontpage(request):
    return render(request, 'frontpage.html',)

def dashboard(request):
    incomeData = IncomeDetails.objects.all()
    expensesData = ExpenditureDetails.objects.all()
    
    # Calculate total income here
    total_income = IncomeDetails.objects.aggregate(total=Sum('amount'))['total'] or 0.0
     # Calculate total expenditure here
    total_expenses = ExpenditureDetails.objects.aggregate(total=Sum('amount'))['total'] or 0.0
  
    values = total_income - total_expenses
    result = "Total Loss" if values < 0 else ("Total Profit" if values > 0 else "Nill")



    context = {
        'income': incomeData,
        'expenses': expensesData,
        'total_income': total_income,  
        'total_expenses': total_expenses,
        'values': values,
        'result': result,
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


def delete_income(request, income_id):
    income = IncomeDetails.objects.get(id = income_id)
    income.delete()
    messages.success(request, 'Income record deleted successfully', extra_tags='income')
    return redirect('/dashboard')


def delete_expenditure(request, expenditure_id):
    expenditure = ExpenditureDetails.objects.get(id=expenditure_id)
    expenditure.delete()
    messages.success(request, 'Expenditure record deleted successfully', extra_tags='expenditure')
    return redirect('/dashboard')


def edit_income(request, income_id):
    income = IncomeDetails.objects.get(id=income_id)
    form = IncomForm(instance=income)  # Initialize the form here

    if request.method == 'POST':
        form = IncomForm(request.POST, instance=income)  # Update with POST data
        if form.is_valid():
            form.save()
            messages.add_message(request, messages.SUCCESS, 'Income Details Updated Successfully')
            return redirect('/dashboard')
        else:
            messages.add_message(request, messages.ERROR, 'Failed to Update Details')

    context = {
        'form': form
    }
    return render(request, 'editincomedetails.html', context)

