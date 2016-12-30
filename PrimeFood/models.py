from django.db import models


class Menu(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField(max_length=2000, blank=True, null=True)

    def __str__(self):
        return self.title


class MenuCategory(models.Model):
    menu = models.ForeignKey(Menu, on_delete=models.CASCADE, default=None)
    title = models.CharField(max_length=200)
    description = models.TextField(max_length=2000, blank=True, null=True)

    def __str__(self):
        return self.title


class MenuItem(models.Model):
    price = models.FloatField()
    amount = models.CharField(max_length=200)
    menucategory = models.ForeignKey(MenuCategory, on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    description = models.TextField(max_length=2000, blank=True, null=True)

    def __str__(self):
        return self.title

    def get_menu(self):
        return self.menucategory.menu
