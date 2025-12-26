from django.contrib import admin
from .models import Expense, Category

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ['name', 'user', 'color', 'icon']
    list_filter = ['user']
    search_fields = ['name']

@admin.register(Expense)
class ExpenseAdmin(admin.ModelAdmin):
    list_display = ['title', 'amount', 'category', 'date', 'user', 'payment_method']
    list_filter = ['category', 'payment_method', 'date']
    search_fields = ['title', 'notes']
    date_hierarchy = 'date'
