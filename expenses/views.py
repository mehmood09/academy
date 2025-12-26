from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.db.models import Sum, Count
from django.db.models.functions import TruncMonth
from datetime import datetime, timedelta
from .models import Expense, Category
from .forms import ExpenseForm, CategoryForm

@login_required
def dashboard(request):
    today = datetime.now().date()
    start_of_month = today.replace(day=1)
    
    # Statistics
    total_expenses = Expense.objects.filter(user=request.user).aggregate(Sum('amount'))['amount__sum'] or 0
    month_expenses = Expense.objects.filter(user=request.user, date__gte=start_of_month).aggregate(Sum('amount'))['amount__sum'] or 0
    expense_count = Expense.objects.filter(user=request.user).count()
    
    # Recent expenses
    recent_expenses = Expense.objects.filter(user=request.user)[:5]
    
    # Category breakdown
    category_breakdown = Expense.objects.filter(user=request.user).values('category__name', 'category__color').annotate(total=Sum('amount')).order_by('-total')[:5]
    
    # Monthly trend (last 6 months)
    six_months_ago = today - timedelta(days=180)
    monthly_data = Expense.objects.filter(
        user=request.user, 
        date__gte=six_months_ago
    ).annotate(month=TruncMonth('date')).values('month').annotate(total=Sum('amount')).order_by('month')
    
    context = {
        'total_expenses': total_expenses,
        'month_expenses': month_expenses,
        'expense_count': expense_count,
        'recent_expenses': recent_expenses,
        'category_breakdown': category_breakdown,
        'monthly_data': monthly_data,
    }
    return render(request, 'expenes/dashboard.html', context)

@login_required
def expense_list(request):
    expenses = Expense.objects.filter(user=request.user)
    
    # Filter by category
    category_id = request.GET.get('category')
    if category_id:
        expenses = expenses.filter(category_id=category_id)
    
    # Filter by date range
    start_date = request.GET.get('start_date')
    end_date = request.GET.get('end_date')
    if start_date:
        expenses = expenses.filter(date__gte=start_date)
    if end_date:
        expenses = expenses.filter(date__lte=end_date)
    
    categories = Category.objects.filter(user=request.user)
    total = expenses.aggregate(Sum('amount'))['amount__sum'] or 0
    
    context = {
        'expenses': expenses,
        'categories': categories,
        'total': total,
    }
    return render(request, 'expenes/expense_list.html', context)

@login_required
def expense_create(request):
    if request.method == 'POST':
        form = ExpenseForm(request.POST)
        if form.is_valid():
            expense = form.save(commit=False)
            expense.user = request.user
            expense.save()
            messages.success(request, 'Expense added successfully!')
            return redirect('expense_list')
    else:
        form = ExpenseForm()
    
    form.fields['category'].queryset = Category.objects.filter(user=request.user)
    return render(request, 'expenes/expense_form.html', {'form': form, 'title': 'Add Expense'})

@login_required
def expense_update(request, pk):
    expense = get_object_or_404(Expense, pk=pk, user=request.user)
    if request.method == 'POST':
        form = ExpenseForm(request.POST, instance=expense)
        if form.is_valid():
            form.save()
            messages.success(request, 'Expense updated successfully!')
            return redirect('expense_list')
    else:
        form = ExpenseForm(instance=expense)
    
    form.fields['category'].queryset = Category.objects.filter(user=request.user)
    return render(request, 'expenes/expense_form.html', {'form': form, 'title': 'Edit Expense'})

@login_required
def expense_delete(request, pk):
    expense = get_object_or_404(Expense, pk=pk, user=request.user)
    if request.method == 'POST':
        expense.delete()
        messages.success(request, 'Expense deleted successfully!')
        return redirect('expense_list')
    return render(request, 'expenes/expense_confirm_delete.html', {'expense': expense})

@login_required
def category_list(request):
    categories = Category.objects.filter(user=request.user)
    return render(request, 'expenes/category_list.html', {'categories': categories})

@login_required
def category_create(request):
    if request.method == 'POST':
        form = CategoryForm(request.POST)
        if form.is_valid():
            category = form.save(commit=False)
            category.user = request.user
            category.save()
            messages.success(request, 'Category created successfully!')
            return redirect('category_list')
    else:
        form = CategoryForm()
    return render(request, 'expenes/category_form.html', {'form': form, 'title': 'Add Category'})
