from django.shortcuts import render, get_object_or_404
from products.models import Category, Product

# Create your views here.


def index(request, category_slug=None):
    category_page = None
    products = None
    if category_slug != None:
        category_page = get_object_or_404(Category, slug=category_slug)
        products = Product.objects.filter(
            category=category_page, available=True)
    else:
        products = Product.objects.all().filter(available=True)
    return render(request, 'index.html', {'category': category_page, 'products': products})


def search(request):
    products = Product.objects.filter(name__contains=request.GET['title'])
    return render(request, 'products.html', {'products': products})
