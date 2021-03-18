from django.contrib import admin
from .models import CategoryProductModel, ProductModel, CartProductModel




@admin.register(CategoryProductModel)
class CategoryProductAdmin(admin.ModelAdmin):
    list_display = ['category_name', 'category_slug']
    prepopulated_fields = {'category_slug': ('category_name',)}

@admin.register(ProductModel)
class ProductAdmin(admin.ModelAdmin):
    list_display = ['category', 'product_name', 'product_price', 'product_description', 'product_available' ]
    list_editable = ['product_price', 'product_available']
    prepopulated_fields = {'product_slug': ('product_name',)}


@admin.register(CartProductModel)
class CartProductAdmin(admin.ModelAdmin):
    list_display = ['product', 'quantity']
    list_editable = ['quantity']
