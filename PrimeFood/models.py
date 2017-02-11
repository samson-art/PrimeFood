from django.db import models


class Menu(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField(max_length=2000, blank=True, null=True)
    order = models.IntegerField(blank=True, null=True, default=0)
    first = models.BooleanField(default=False)

    def __str__(self):
        return self.title

    def first(self):
       if self.first is True:
           return 'first'
       else:
           return ''


class MenuCategory(models.Model):
    menu = models.ForeignKey(Menu, on_delete=models.CASCADE, default=None)
    title = models.CharField(max_length=16)
    description = models.TextField(max_length=2000, blank=True, null=True)
    order = models.IntegerField(blank=True, null=True, default=0)

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

    def __str__(self):
        return self.title

    def get_menu(self):
        return self.menucategory.menu

    def get_by_category(self, mc):
        return MenuItem.objects.filter(menucategory=mc)
