from django.shortcuts import render
from store.models import Product, Category


def main_view(request):
    if request.method == 'GET':
        return render(request, 'layouts/index.html')


def products_view(request):
    if request.method == 'GET':
        category_id = request.GET.get("category_id")
        if category_id:
            products = Product.objects.filter(category_id=category_id)
        else:
            products = Product.objects.all()
        data = {
            'products': products,
        }
        return render(request, 'products/products.html', context=data)


def product_detail_view(request, id):
    if request.method == 'GET':
        product = Product.objects.get(id=id)
        data = {
            'product': product,
            'reviews': product.review_set.all(),
            'categories':product.category
        }
        return render(request, 'products/detail.html', context=data)


def categories_view(request):
    if request.method == "GET":
        categories = Category.objects.all()
        data = {
            'categories': categories
        }
        return render(request, 'categories/index.html', context=data)
