from django.contrib import admin
from .models import Menu, MenuCategory, MenuItem


@admin.register(Menu)
class MenuAdmin(admin.ModelAdmin):
    list_display = ('title', 'first', 'description', 'order')
    search_fields = ['title']


@admin.register(MenuCategory)
class MenuCategoryAdmin(admin.ModelAdmin):
    list_display = ('title', 'description', 'menu', 'order')
    search_fields = ['title']


@admin.register(MenuItem)
class MenuItemAdmin(admin.ModelAdmin):
    list_display = ('title', 'menu', 'menucategory', 'price', 'amount', 'description', 'order')
    search_fields = ['title']
