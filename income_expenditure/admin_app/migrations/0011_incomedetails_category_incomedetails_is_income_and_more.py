# Generated by Django 5.1.7 on 2025-03-29 20:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('admin_app', '0010_expendituredetails'),
    ]

    operations = [
        migrations.AddField(
            model_name='incomedetails',
            name='category',
            field=models.CharField(blank=True, max_length=255),
        ),
        migrations.AddField(
            model_name='incomedetails',
            name='is_income',
            field=models.BooleanField(default=True),
        ),
        migrations.AddField(
            model_name='incomedetails',
            name='notes',
            field=models.TextField(blank=True),
        ),
        migrations.AddField(
            model_name='incomedetails',
            name='sub_category',
            field=models.CharField(blank=True, max_length=255),
        ),
        migrations.AddField(
            model_name='incomedetails',
            name='transaction_type',
            field=models.CharField(blank=True, max_length=255),
        ),
    ]
