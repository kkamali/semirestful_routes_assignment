from django.shortcuts import render, redirect, reverse
from . import models

# Create your views here.
def index(request):
    products = models.Product.objects.all()
    context = { 'products' : products }
    return render(request, "semirestfulroutes/index.html", context)

def show(request, product):
    display_product = models.Product.objects.get(pk = product)
    context = { 'product' : display_product}
    return render(request, "semirestfulroutes/show.html", context)

def edit(request, product):
    context = { 'product' : product }
    return render(request, "semirestfulroutes/edit.html", context)

def update(request, product):
    edit_product = models.Product.objects.get(pk = product)
    if request.POST['name']:
        edit_product.name = request.POST['name']
        edit_product.save()
    if request.POST['description']:
        edit_product.description = request.POST['description']
        edit_product.save()
    if request.POST['price']:
        edit_product.price = request.POST['price']
        edit_product.save()
    return redirect(reverse("show", kwargs={'product': product }))

def remove(request, product):
    remove_product = models.Product.objects.get(pk = product)
    remove_product.delete()
    return redirect(reverse("index"))

def add(request):
    return render(request, "semirestfulroutes/add.html")

def create(request):
    name = request.POST['name']
    description = request.POST['description']
    price = request.POST['price']
    product = models.Product(name = name, description = description, price = price)
    product.save()
    return redirect(reverse("index"))
