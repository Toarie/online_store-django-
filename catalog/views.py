from django.shortcuts import render, get_object_or_404
from .models import Product, Category

def home(request):
    products = Product.objects.filter(in_stock=True).order_by('-created_at')[:8]
    return render(request, 'catalog/home.html', {
        'products': products,
        'categories': Category.objects.all()
    })

def contacts(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        phone = request.POST.get('phone')
        message = request.POST.get('message')
        print(f'Новое сообщение от {name} ({phone}): {message}')
    return render(request, 'catalog/contacts.html')

def product_detail(request, pk):
    product = get_object_or_404(Product, pk=pk, in_stock=True)
    return render(request, 'catalog/product_detail.html', {
        'product': product,
        'similar_products': Product.objects.filter(
            category=product.category,
            in_stock=True
        ).exclude(pk=pk)[:4]
    })

