from django.shortcuts import render
from products.models import Product, Category


def home(request):
    categories = Category.objects.all()
    products = Product.objects.all().order_by('-id')[:6]
    latest_products = Product.objects.order_by('-category')[:4]
    context = {
        'categories': categories,
        'products': products,
        'latest_products': latest_products,

    }
    return render(request, 'ritzy/index.html', context)