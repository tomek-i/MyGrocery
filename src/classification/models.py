from django.db import models
from django.utils.translation import ugettext_lazy as _
from django.utils.text import slugify

# Create your models here.


class Tag(models.Model):
    """ A tag """
    # CHOICES

    # DB FIELDS
    name = models.CharField(_('name'), max_length=50)
    created_at = models.DateTimeField(auto_now_add=True)
    last_updated = models.DateTimeField(auto_now=True)

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


class Category(models.Model):
    """ A Food category """
    # CHOICES

    # DB FIELDS
    name = models.CharField(_('name'), max_length=50, unique=True)
    slug = models.SlugField(unique=True)

    desc = models.TextField(_("description"))
    parent = models.ForeignKey(
        'self',
        verbose_name=_('parent'),
        related_name='categories',
        on_delete=models.CASCADE,
        null=True)

    created_at = models.DateTimeField(_('created at'), auto_now_add=True)
    last_updated = models.DateTimeField(_('last updated'), auto_now=True)

    # MANAGERS

    # META
    class Meta:
        # TODO: add verbose_plural name
        verbose_name_plural = 'categories'
        pass

    # __STR__
    def __str__(self):
        return self.name

    # SAVE
    def save(self, *args, **kwargs):
        self.slug = slugify(self.name.replace('&', 'and'))
        # TODO: can that be just super() ?
        super(Category, self).save(*args, **kwargs)
    # ABSOLUTE URL

    # METHODS
