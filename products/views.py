from django.shortcuts import render

# Create your views here.


def productPage(request):
    return render(request, 'product.html')


def allProducts(request):
    return render(request, 'products.html')
