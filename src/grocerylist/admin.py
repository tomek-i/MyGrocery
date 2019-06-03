from django.contrib import admin
from .models import ShoppingList,  Item, Product, Supermarket, Supermarket_Product

# Register your models here.

"""


class ItemsOnShoppinglist(admin.TabularInline):
    model = ShoppingBasket
    extra = 1
"""


class ProductsInSupermarket(admin.TabularInline):
    model = Supermarket_Product
    extra = 1


@admin.register(ShoppingList)
class ShoppingListAdmin(admin.ModelAdmin):
    list_display = ('name', 'is_completed_icon', 'item_count',
                    'item_count_completed', 'item_count_missing')
    #inlines = [ItemsOnShoppinglist]

    def item_count(self, obj, *args, **kwargs):
        return obj.items.count()
    item_count.short_description = 'total items'

    def item_count_completed(self, obj, *args, **kwargs):
        return obj.items.filter(cart__completed=True).count()
    item_count_completed.short_description = 'completed'

    def item_count_missing(self, obj, *args, **kwargs):
        return obj.items.filter(cart__completed=False).count()
    item_count_missing.short_description = 'missing'

    def is_completed_icon(self, obj):
        return obj.is_completed()
    is_completed_icon.boolean = True
    is_completed_icon.short_description = 'completed ?'
    is_completed_icon.admin_order_field = 'is_completed'


@admin.register(Item)
class ItemAdmin(admin.ModelAdmin):
    list_display = ('name', 'category')
    pass


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    pass


@admin.register(Supermarket_Product)
class ProductsInSupermarketAdmin(admin.ModelAdmin):
    list_display = ('product', 'price', 'store', 'code', 'short_name')
    pass


@admin.register(Supermarket)
class StoreAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'address')
    list_display_links = ('id', 'name')
    ordering = ['id', ]
    inlines = [ProductsInSupermarket]
    pass
