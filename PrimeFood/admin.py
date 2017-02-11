from django.contrib import admin
from django import forms
from .models import Menu, MenuCategory, MenuItem


class CategoryInLine(admin.StackedInline):
    model = MenuCategory
    extra = 0
    exclude = []
    verbose_name = ''


class ItemsInLine(admin.StackedInline):
    model = MenuItem
    extra = 0
    exclude = ['menu']
    verbose_name = ''


class CategoryForm(forms.ModelForm):
    pass
    # class Meta:
    #     model = MenuCategory


class ItemForm(forms.ModelForm):
    class Meta:
        model = MenuItem
        exclude = ['menu', 'menucategory']


@admin.register(Menu)
class MenuAdmin(admin.ModelAdmin):
    list_display = ('title', 'first', 'description', 'order')
    search_fields = ['title']
    inlines = [CategoryInLine]


@admin.register(MenuCategory)
class MenuCategoryAdmin(admin.ModelAdmin):
    list_display = ('title', 'description', 'menu', 'order')
    search_fields = ['title']
    ordering = ['menu', 'order']
    form = CategoryForm
    list_filter = (
        ('menu', admin.RelatedOnlyFieldListFilter),
    )
    inlines = [ItemsInLine]
    radio_fields = {"menu": admin.HORIZONTAL}


@admin.register(MenuItem)
class MenuItemAdmin(admin.ModelAdmin):
    search_fields = ['title']
    form = ItemForm
    ordering = ['menu', 'menucategory', 'order']
    list_filter = (
        ('menucategory', admin.RelatedOnlyFieldListFilter),
    )
    list_per_page = 20
    radio_fields = {"menucategory": admin.VERTICAL}
    readonly_fields = ['menu', 'menucategory']
    list_display = ('title', 'menu', 'menucategory', 'price', 'amount', 'description', 'order')
    fieldsets = (
        (None, {'fields': ('title', 'amount', 'price')}),
        ('Menu', {'fields': ('menu', 'menucategory')}),
        (None, {'fields': ('description', 'order')})
    )
