# Generated by Django 5.1.7 on 2025-03-25 19:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('admin_app', '0004_rename_source_of_income_expendituredetails_source_of_expenditure_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='incomedetails',
            name='date',
            field=models.DateField(),
        ),
    ]
