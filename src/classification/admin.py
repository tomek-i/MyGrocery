from django.contrib import admin
from .models import Tag, Category

# Register your models here.


class Subcategories(admin.TabularInline):
    model = Category
    extra = 1
    prepopulated_fields = {'slug': ('name',)}


@admin.register(Tag)
class TagAdmin(admin.ModelAdmin):
    pass


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    # TODO: add inlines to create subcategories
    # TODO: hide parent
    list_display = ('name', 'slug', 'parent')
    prepopulated_fields = {'slug': ('name',)}
    fields = ['parent', 'name', 'slug', 'desc']
    inlines = [Subcategories, ]
    pass
