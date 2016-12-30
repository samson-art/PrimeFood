from django.contrib import admin
from .models import Menu, MenuCategory, MenuItem

@admin.register(Menu)
class MenuAdmin(admin.ModelAdmin):
    pass

@admin.register(MenuCategory)
class MenuCategoryAdmin(admin.ModelAdmin):
    pass

@admin.register(MenuItem)
class MenuItemAdmin(admin.ModelAdmin):
    pass