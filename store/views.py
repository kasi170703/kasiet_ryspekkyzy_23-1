from django.shortcuts import render
from store.models import Product


def main_view(request):
    if request.method == 'GET':
        return render(request, 'layouts/index.html')


def products_view(request):
    if request.method == 'GET':
        products = Product.objects.all()
        data = {
            'products': products
        }
        return render(request, 'products/products.html', context=data)


def product_detail_view(request, **kwargs):
    if request.method == 'GET':
        product = Product.objects.get(id=kwargs['id'])
        data = {
            'product': product ,
            'reviews': product.review_set.all()
        }
        return render(request, 'products/detail.html', context=data)


