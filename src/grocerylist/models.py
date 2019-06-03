from django.db import models
from django.utils.translation import ugettext_lazy as _

from classification.models import Category, Tag
# Create your models here.
#from classification.models import Tag, Category


class Item(models.Model):
    """ An item / to put on the grocery list """
    # CHOICES

    # DB FIELDS
    name = models.CharField(_('name'), max_length=50)

    created_at = models.DateTimeField(_('created at'), auto_now_add=True)
    last_updated = models.DateTimeField(_('last updated'), auto_now=True)

    category = models.ForeignKey(Category, verbose_name=_(
        'category'), default=None, blank=True, null=True, related_name='items', on_delete=models.CASCADE)
    # MANAGERS

    # META
    class Meta:
        pass

    # __STR__
    def __str__(self):
        return self.name

    # SAVE

    # ABSOLUTE URL

    # METHODS
    # def is_completed(self):
    #    return self.cart.get(id=self.id).completed


class Product(models.Model):
    """ a product which can be bought at a supermarket for a specific price asked by the supermarket """
    # CHOICES

    # DB FIELDS

    name = models.CharField(_('name'), max_length=50)
    brand = models.CharField(_('brand'), max_length=50)

    # TODO: need to find out if barcodes are unique to store or to product, i would assume to product
    # NOTE: should mark as unique ?
    barcode = models.CharField(_('barcode'), max_length=100, blank=True)

    created_at = models.DateTimeField(_('created at'), auto_now_add=True)
    last_updated = models.DateTimeField(_('last updated'), auto_now=True)

    item_type = models.ForeignKey(Item, verbose_name=_(
        'type'), related_name='products', on_delete=models.CASCADE, blank=True, null=True)
    # MANAGERS

    # META

    class Meta:
        pass

    # __STR__
    def __str__(self):
        return f'{self.brand} {self.name}'

    # SAVE

    # ABSOLUTE URL

    # METHODS


class Supermarket(models.Model):
    """ the supermarket which contains a list of products"""
    # CHOICES

    # DB FIELDS
    name = models.CharField(_('name'), max_length=50)
    address = models.CharField(_('address'), blank=True, max_length=50)

    created_at = models.DateTimeField(_('created at'), auto_now_add=True)
    last_updated = models.DateTimeField(_('last updated'), auto_now=True)

    # , through='StoreProduct')
    products = models.ManyToManyField(
        Product,  through='Supermarket_Product', blank=True)

    # MANAGERS

    # META
    class Meta:
        pass

    # __STR__
    def __str__(self):
        return self.name

    # SAVE

    # ABSOLUTE URL

    # METHODS


class ShoppingList(models.Model):
    """ This is the grocery / shopping list you create """
    # CHOICES

    # DB FIELDS
    name = models.CharField(_('name'), max_length=50)

    # through='ShoppingBasket')
    items = models.ManyToManyField(
        Item, related_name='shoppinglist', blank=True)

    created_at = models.DateTimeField(_('created at'), auto_now_add=True)
    last_updated = models.DateTimeField(_('last updated'), auto_now=True)

    # MANAGERS

    # META
    class Meta:
        verbose_name = _('Shopping List')
        verbose_name_plural = _('Shopping Lists')
        pass

    # __STR__
    def __str__(self):
        return self.name

    # SAVE

    # ABSOLUTE URL

    # METHODS

    def is_completed(self):
        return self.items.filter(cart__completed=False).count() == 0


class Supermarket_Product(models.Model):
    # CHOICES

    # DB FIELDS
    product = models.ForeignKey(Product, verbose_name=_(
        'product'), on_delete=models.CASCADE)

    store = models.ForeignKey(Supermarket, verbose_name=_(
        'supermarket'), on_delete=models.CASCADE)

    price = models.DecimalField(_('price'), max_digits=5, decimal_places=2)
    short_name = models.CharField(
        _('short name'), unique=True, max_length=30, blank=True)
    code = models.CharField(_("code"), unique=True, max_length=30, blank=True)

    created_at = models.DateTimeField(auto_now_add=True)
    last_updated = models.DateTimeField(auto_now=True)

    # MANAGERS

    # META

    class Meta:
        pass

    # __STR__
    def __str__(self):
        return f'{self.product} {self.price} - {self.store}'

    # SAVE

    # ABSOLUTE URL

    # METHODS


"""
class GroceryList_Item(models.Model):

    # NOTE: or rename to shopping cart
    # CHOICES

    # DB FIELDS
    #item = models.ForeignKey(        Item, on_delete=models.CASCADE, related_name='cart')

    #grocerylist = models.ForeignKey(GroceryList, on_delete=models.CASCADE)

    completed = models.BooleanField(default=False)

    created_at = models.DateTimeField(_('created at'), auto_now_add=True)
    last_updated = models.DateTimeField(_('last updated'), auto_now=True)
    # MANAGERS

    # META
    class Meta:
        pass

    # __STR__
    def __str__(self):
        return ''  # f'{self.item}'

    # SAVE

    # ABSOLUTE URL

    # METHODS
"""
