from django.contrib import admin
from .models import GroceryList,  Item, StoreProducts, Product, Store

# Register your models here.


@admin.register(GroceryList)
class GroceryListAdmin(admin.ModelAdmin):
    pass


@admin.register(Item)
class ItemAdmin(admin.ModelAdmin):
    pass


@admin.register(StoreProducts)
class StoreProductsAdmin(admin.ModelAdmin):
    pass


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    pass


@admin.register(Store)
class StoreAdmin(admin.ModelAdmin):
    pass
