from django.contrib import admin
from .models import IncomeExpense

@admin.register(IncomeExpense)
class IncomeExpenseAdmin(admin.ModelAdmin):
    list_display = ('date', 'source', 'amount', 'is_income')
    list_filter = ('is_income', 'date')
    search_fields = ('source',)