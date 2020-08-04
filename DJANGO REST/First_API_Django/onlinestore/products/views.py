from django.http import JsonResponse
from .models import Product, Manufacturer

def product_list(request):
    products = Product.objects.all() # product query set
    data = {"products": list(products.values("pk", "name"))} # use of query set with JsonResponse ++ you can choose whatever values you want to list
    response = JsonResponse(data)
    return response

def product_detail(request, pk):
    try:
        product = Product.objects.get(pk=pk)
        data = {"product" : {
                    "name" : product.name,
                    "manufacturer" : product.manufacturer.name,
                    "description" : product.description,
                    "photo" : product.photo.url,
                    "price" : product.price ,
                    "shipping_cost" : product.shipping_cost,
                    "quantity" : product.quantity,
        }}
        response = JsonResponse(data)
    except Product.DoesNotExist:
        response = JsonResponse({
            "error" : {     # for users
                "code" : 404,
                "message" : "product not found!"
            }},
            status = 404) # to inform the client does not exist
    return response

# COMPETENCY ASSESEMENT 

def manufacturer_detail(request,id):
    try:
        manufacturer = Manufacturer.objects.get(id=id)
        manufacturer_products = manufacturer.products.all()
        data = {"manufacturer" : {
                    "name" : manufacturer.name,
                    "location" : manufacturer.location,
                    "active" : manufacturer.active,
                    "products" : list(manufacturer_products.values())
        }}
        response = JsonResponse(data)
    except Manufacturer.DoesNotExist:
        response = JsonResponse({
            "error" : {    
                "code" : 404,
                "message" :  "manufacturer not found!"
            }},
            status = 404) 
    return response

def manufacturer_active(request):
    manufacturers = Manufacturer.objects.filter(active=True)
    data = {"manufacturers": list(manufacturers.values("id", "name", "location"))}  
    response = JsonResponse(data)
    return response






# INITIAL PART 
""" 
from django.views.generic.detail import DetailView
from django.views.generic.list import ListView

class ProductDetailView(DetailView):
    model = Product
    template_name = "products/product_detail.html"

class ProductListView(ListView):
    model = Product
    template_name = "products/product_list.html"
 """