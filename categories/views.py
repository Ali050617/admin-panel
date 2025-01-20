from django.shortcuts import render, get_object_or_404, redirect
from django.db.models import Count, Sum
from .models import Category
from .forms import CategoryForm
from products.models import Product
from orders.models import Order


def dashboard(request):
    total_products = Product.objects.count()
    total_categories = Category.objects.count()
    total_orders = Order.objects.count()
    recent_products = Product.objects.all().order_by('-created_at')[:9]
    categories = Category.objects.all()

    max_products = 1000  # You can adjust this value based on your needs
    product_scale_percentage = min((total_products / max_products) * 100, 100)

    context = {
        'total_products': total_products,
        'total_categories': total_categories,
        'total_orders': total_orders,
        'recent_products': recent_products,
        'categories': categories,
        'product_scale_percentage': product_scale_percentage,
    }
    return render(request, 'index.html', context)


def category_list(request):
    categories = Category.objects.all()
    return render(request, 'categories/list.html', {'categories': categories})


def category_detail(request, pk):
    category = get_object_or_404(Category, pk=pk)
    return render(request, 'categories/detail.html', {'category': category})


def category_create(request):
    if request.method == 'POST':
        form = CategoryForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('categories:category_list')
    else:
        form = CategoryForm()
    return render(request, 'categories/form.html', {'form': form})


def category_update(request, pk):
    category = get_object_or_404(Category, pk=pk)
    if request.method == 'POST':
        form = CategoryForm(request.POST, request.FILES, instance=category)
        if form.is_valid():
            form.save()
            return redirect('categories:category_list')
    else:
        form = CategoryForm(instance=category)
    return render(request, 'categories/form.html', {'form': form, 'category': category})


def category_delete(request, pk):
    category = get_object_or_404(Category, pk=pk)
    if request.method == 'POST':
        category.delete()
        return redirect('categories:category_list')
    return render(request, 'categories/delete-confirm.html', {'category': category})
