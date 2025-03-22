from django.db import models

class IncomeExpense(models.Model):
    date = models.DateField()
    source = models.CharField(max_length=255)
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    is_income = models.BooleanField(default=True)  # True for income, False for expense

    def __str__(self):
        return f"{self.date} - {self.source} - {self.amount}"