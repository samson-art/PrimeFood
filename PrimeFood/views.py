from django.shortcuts import render
from django.forms.models import model_to_dict
from photologue.models import Gallery
from .models import *


def landing_page(request):
    menu = Menu.objects.all()
    menucat = MenuCategory.objects.all()
    menuitem = MenuItem.objects.all()
    menudata = dict((m.title, {mc.title: {'id': mc.id, 'items':[model_to_dict(mi) for mi in menuitem if mi.menucategory == mc and mi.menucategory.menu == m]} for mc in menucat if mc.menu == m}) for m in menu)
    for m in menu:
        menudata[m.title].update({'id': m.id})
    return render(request, 'landing_page.html', {
        'title': "PrimeFood",
        'slidergallery': Gallery.objects.filter(title='Слайдер').first().photos.all(),
        'gallery': Gallery.objects.filter(title='Галлерея').first().photos.all(),
        'menudata': menudata
    })
