from django.forms import ModelForm
from . models import *

class IncomForm(ModelForm):
    class Meta:
        model = IncomeDetails
        fields = '__all__'

class ExpenditureForm(ModelForm):
    class Meta:
        model = ExpenditureDetails
        fields = '__all__'
