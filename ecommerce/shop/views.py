from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse
from django.template import loader

from ecommerce.shop.models import Product

products = Product.objects.all()

def index(request):
    return render(template_name="index.html", request=request, context={'product': products})

def register_product(request):
    if request.method == "GET":
        return render(template_name="register.html", request=request)
    elif request.method == "POST":
        if request.POST.get('active') == 'on':
            active = True
        else:
            active = False
        product = Product()
        product.name = request.POST.get('name', None)
        product.inventory = request.POST.get('inventory', None)
        product.unity_price = request.POST.get('unity_price', None)
        product.image = request.POST.get('image', None)
        product.active = active
        product.save()
        return render(template_name="index.html", request=request, context={'product': products})
    
def find_product(request, name):
    if request.method == "GET":
        finder = Product.objects.filter(name = name)
        return render(request, "index.html", {"product": finder})
    return render(request, "index.html", {"product": products, "erro": "Product não encontrado."})

def delete_product(request, id):
    if request.method == "GET":
        product = Product.objects.filter(id=id)
        product.delete()
        return render(request, "index.html", {"product": products})
    return render(request, "index.html", {"product": products})

def edit(request, id):
    product = Product.objects.get(id=id)
    template = loader.get_template('edit.html')
    context = {
        'product': product,
    }
    return HttpResponse(template.render(context, request))
  
def update_product(request, id):
    name = request.POST['name']
    inventory = request.POST['inventory']
    unity_price = request.POST['unity_price']
    active = True
    product = Product.objects.get(id=id)
    product.name = name
    product.inventory = inventory
    product.unity_price = unity_price
    product.active = active
    product.save()
    return HttpResponseRedirect(reverse('index'))