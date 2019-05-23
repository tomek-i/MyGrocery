from django.contrib import admin
from .models import Tag, Category

# Register your models here.


@admin.register(Tag)
class TagAdmin(admin.ModelAdmin):
    pass


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    # TODO: add inlines to create subcategories
    # TODO: hide parent
    pass
