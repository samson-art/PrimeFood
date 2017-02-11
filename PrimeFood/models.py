from django.db import models


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

    def get_menu(self):
        return self.menucategory.menu

    def get_by_category(self, mc):
        return MenuItem.objects.filter(menucategory=mc)
