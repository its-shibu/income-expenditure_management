from django.urls import path
from . import views

urlpatterns = [
    path('', views.frontpage),
    path('dashboard/', views.dashboard, name='dashboard'),
    path('addincome/', views.addIncome, name='add_income'), 
    path('addexpenditure/', views.addExpenditure, name='add expenditure'),
    path('dltincome/<int:income_id>/', views.delete_income, name='delete_income'),
    path('dltexpenditure/<int:expenditure_id>/', views.delete_expenditure, name='delete_expenditure'),
    path('editincome/<int:income_id>/', views.edit_income, name = 'edit_income'),
    path('editexpenses/<int:expenditure_id>/', views.edit_expenditure, name='edit_expenditure'),

]