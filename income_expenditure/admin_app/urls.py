from django.urls import path
from . import views

urlpatterns = [
    path('', views.frontpage),
    path('dashboard/', views.dashboard, name='dashboard'),
    path('addincome/', views.addIncome, name='add income'), 
    path('addexpenditure/', views.addExpenditure, name='add expenditure')
]