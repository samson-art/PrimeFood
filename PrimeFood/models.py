from django.db import models
from django.urls import reverse
from django.utils.safestring import mark_safe


class Menu(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField(max_length=2000, blank=True, null=True)
    order = models.IntegerField(blank=True, null=True, default=0)
    first = models.BooleanField(default=False)

    class Meta:
        verbose_name = 'Menu'
        verbose_name_plural = 'Menu'
        ordering = ['order']

    def __str__(self):
        return self.title

    def display_categories(self):
        return ', '.join(["<a href='%s'>%s</a>" % (reverse('admin:PrimeFood_menucategory_change', args=[c.id]), c.title) for c in MenuCategory.objects.filter(menu=self)])

    display_categories.allow_tags = True
    display_categories.short_description = 'Categories'


class MenuCategory(models.Model):
    menu = models.ForeignKey(Menu, on_delete=models.CASCADE, default=None)
    title = models.CharField(max_length=16)
    description = models.TextField(max_length=2000, blank=True, null=True)
    order = models.IntegerField(blank=True, null=True, default=0)

    class Meta:
        verbose_name = 'Category'
        verbose_name_plural = 'Categories'
        ordering = ['order']

    def __str__(self):
        return self.title

    def get_by_menu(self, menu):
        return MenuCategory.objects.filter(menu=menu)

    def display_items(self):
        return ', '.join(['<a href="%s">%s</a>' % (reverse('admin:PrimeFood_menuitem_change', args=[i.id]), i.title) for i in MenuItem.objects.filter(menucategory=self)])

    display_items.short_description = 'Items'
    display_items.allow_tags = True

    def show_menu(self):
        return mark_safe('<a href="%s">%s</a>' % (reverse('admin:PrimeFood_menu_change', args=[self.menu.id]), self.menu.title))
    show_menu.allow_tags = True
    show_menu.short_description = 'Menu'


class MenuItem(models.Model):
    price = models.DecimalField(max_digits=8, decimal_places=2)
    amount = models.CharField(max_length=200)
    menucategory = models.ForeignKey(MenuCategory, on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    description = models.TextField(max_length=2000, blank=True, null=True)
    menu = models.ForeignKey(Menu, on_delete=models.CASCADE, blank=True, null=True)
    order = models.IntegerField(blank=True, null=True, default=0)

    class Meta:
        verbose_name = 'Item'
        verbose_name_plural = 'Items'
        ordering = ['order']

    def __str__(self):
        return self.title

    def display_menu_list(self):
        return Menu.objects.all()
    display_menu_list.short_description = 'Menu'

    def display_categories_list(self):
        return MenuCategory.objects.filter(menu=self.menu)
    display_categories_list.short_description = 'Categories'
