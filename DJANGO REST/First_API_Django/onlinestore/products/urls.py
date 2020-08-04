from django.urls import path
from .views import manufacturer_active, manufacturer_detail, product_detail, product_list
# FIRST VERSION: from .views import ProductDetailView, ProductListView 

# Define URL patterns

urlpatterns = [
    path("products/", product_list, name="product-list"),
    path("products/<int:pk>/", product_detail, name="product-detail"),
    path("manufacturer/<int:id>", manufacturer_detail, name="manufacturer-detail"),
    path("manufacturer/active", manufacturer_active, name="manufacturer-active"),
]
