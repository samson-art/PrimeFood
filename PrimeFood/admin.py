from django.contrib import admin
from django import forms
from django.urls import reverse
from django.utils.safestring import mark_safe

from .models import Menu, MenuCategory, MenuItem


class CategoryInLine(admin.TabularInline):
    model = MenuCategory
    extra = 0
    exclude = []
    verbose_name = ''
    fields = ['order', 'title', 'description', 'show_category']
    readonly_fields = ['show_category']

    def show_category(self, obj):
        url = reverse("admin:PrimeFood_menucategory_change", args=[obj.id])
        return mark_safe('<a class="grp-button grp-default" href="%s">Show</a>' % url)

    show_category.allow_tags = True


class ItemsInLine(admin.StackedInline):
    model = MenuItem
    extra = 0
    exclude = ['menu']
    verbose_name = ''
    fields = [('title', 'show_item'), ('amount', 'price'), 'description', 'order']
    readonly_fields = ['show_item']

    def show_item(self, obj):
        url = reverse("admin:PrimeFood_menuitem_change", args=[obj.id])
        return mark_safe('<a class="grp-button grp-default" href="%s">Show</a>' % url)

    show_item.short_description = ''
    show_item.allow_tags = True


class CategoryForm(forms.ModelForm):
    pass
    # class Meta:
    #     model = MenuCategory


# class ItemForm(forms.ModelForm):
#     pass


@admin.register(Menu)
class MenuAdmin(admin.ModelAdmin):
    list_display = ('title', 'first', 'description', 'order', 'display_categories')
    search_fields = ['title']
    inlines = [CategoryInLine]
    fieldsets = (
        (None, {'fields': ('title', 'description')}),
        ('Ordering', {'fields': ('first', 'order')}),
    )


@admin.register(MenuCategory)
class MenuCategoryAdmin(admin.ModelAdmin):
    list_display = ('title', 'description', 'show_menu', 'display_items', 'order')
    search_fields = ['title']
    ordering = ['menu', 'order']
    list_filter = ['menu']
    inlines = [ItemsInLine]
    radio_fields = {"menu": admin.HORIZONTAL}


@admin.register(MenuItem)
class MenuItemAdmin(admin.ModelAdmin):
    search_fields = ['title']
    ordering = ['menu', 'menucategory', 'order']
    list_filter = ['menu', 'menucategory']
    list_per_page = 20
    readonly_fields = ['show_menu', 'show_menucategory', 'link_menu', 'link_menucategory']
    list_display = ('title', 'show_menu', 'show_menucategory', 'price', 'amount', 'description', 'order')
    fieldsets = (
        (None, {'fields': ('title', ('amount', 'price'))}),
        ('Menu', {'fields': (('menu', 'link_menu'), ('menucategory', 'link_menucategory'))}),
        (None, {'fields': ('description', 'order')})
    )

    def show_menu(self, obj):
        url = reverse('admin:PrimeFood_menu_change', args=[obj.menu.id])
        return mark_safe('<a href="%s">"%s"</a>' % (url, obj.menu.title))

    show_menu.allow_tags = True
    show_menu.short_description = ''

    def show_menucategory(self, obj):
        url = reverse('admin:PrimeFood_menucategory_change', args=[obj.menucategory.id])
        return mark_safe('<a href="%s">"%s"</a>' % (url, obj.menucategory.title))

    show_menucategory.allow_tags = True
    show_menucategory.short_description = ''

    def link_menucategory(self, obj):
        url = reverse('admin:PrimeFood_menucategory_change', args=[obj.menucategory.id])
        return mark_safe('<a href="%s">"Show"</a>' % (url,))

    link_menucategory.allow_tags = True
    link_menucategory.short_description = ''

    def link_menu(self, obj):
        url = reverse('admin:PrimeFood_menu_change', args=[obj.menu.id])
        return mark_safe('<a href="%s">"Show"</a>' % (url,))

    link_menu.allow_tags = True
    link_menu.short_description = ''
