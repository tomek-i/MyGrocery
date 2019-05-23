from django.db import models
from django.utils.translation import ugettext_lazy as _

# Create your models here.
from classification.models import Tag, Category


class Store(models.Model):
    """ A store """
    # CHOICES

    # DB FIELDS
    name = models.CharField(_('name'), max_length=50)
    # TODO: make address optional
    address = models.CharField(_('address'), max_length=50)

    created_at = models.DateTimeField(_('created at'), auto_now_add=True)
    last_updated = models.DateTimeField(_('last updated'), auto_now=True)

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


class Product(models.Model):
    """ A product is usually linked to a store """
    # CHOICES

    # DB FIELDS

    name = models.CharField(_('name'), max_length=50)

    # TODO: need to find out if barcodes are unique to store or to product, i would assume to product
    barcode = models.CharField(_('barcode'), max_length=100, blank=True)

    created_at = models.DateTimeField(_('created at'), auto_now_add=True)
    last_updated = models.DateTimeField(_('last updated'), auto_now=True)

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


class StoreProducts(models.Model):
    """ each store can contain the same product with different prices """
    # CHOICES

    # DB FIELDS
    product = models.ForeignKey(
        Product,
        verbose_name=_("product"),
        on_delete=models.CASCADE)

    store = models.ForeignKey(
        Store,
        verbose_name=_("store"),
        on_delete=models.CASCADE)

    price = models.DecimalField(_("price"), max_digits=5, decimal_places=2)

    created_at = models.DateTimeField(auto_now_add=True)
    last_updated = models.DateTimeField(auto_now=True)

    # MANAGERS

    # META
    class Meta:
        pass

    # __STR__
    def __str__(self):
        return f'{product} {price} - {store}'

    # SAVE

    # ABSOLUTE URL

    # METHODS


class Item(models.Model):
    """ An item on the grocerylist """
    # CHOICES

    # DB FIELDS
    name = models.CharField(_('name'), max_length=50)

    created_at = models.DateTimeField(_('created at'), auto_now_add=True)
    last_updated = models.DateTimeField(_('last updated'), auto_now=True)

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


class GroceryList(models.Model):
    """ Lists all items on the grocerylist """
    # CHOICES

    # DB FIELDS
    name = models.CharField(_('name'), max_length=50)
    created_at = models.DateTimeField(_('created at'), auto_now_add=True)
    last_updated = models.DateTimeField(_('last updated'), auto_now=True)

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
