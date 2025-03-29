from django.db import models
    


class IncomeDetails(models.Model):
        date = models.DateField()
        source_of_income = models.CharField(max_length=255)
        amount = models.FloatField()
        transaction_type = models.CharField(max_length=255, blank=True)
        notes = models.TextField(blank=True)    
        

class ExpenditureDetails(models.Model):
        date = models.DateField()
        source_of_expenditure = models.CharField(max_length=255)
        amount = models.FloatField()
        transaction_type = models.CharField(max_length=255, blank=True)
        notes = models.TextField(blank=True)  
