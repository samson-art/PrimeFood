from django.shortcuts import render, redirect
from photologue.models import Gallery
from .models import *
import datetime


def get_content():
    menu = Menu.objects.all().order_by('order')
    menucat = MenuCategory.objects.all().order_by('order')
    menuitem = MenuItem.objects.all().order_by('order')
    return menu, menucat, menuitem


def landing_page(request):
    if datetime.datetime.now() < datetime.datetime(2017, 2, 9, 12, 20):
        return render(request, 'timer.html', {
            'start_date': str(datetime.datetime(2017, 2, 9, 12, 20).strftime('%Y/%m/%d %H:%M:%S')),
            'title': 'PrimeFood'
        })
    else:
        menu, menucat, menuitem = get_content()
        return render(request, 'landing_page.html', {
            'title': "PrimeFood",
            'slidergallery': Gallery.objects.filter(title='Слайдер').first().photos.all(),
            'gallery': Gallery.objects.filter(title='Галлерея').first().photos.all(),
            'menu': menu,
            'menucats': menucat,
            'menuitems': menuitem
        })


def demo(request):
    if request.user.is_authenticated():
        menu, menucat, menuitem = get_content()
        return render(request, 'landing_page.html', {
            'title': 'PrimeFood DEMO',
            'slidergallery': Gallery.objects.filter(title='Слайдер').first().photos.all(),
            'gallery': Gallery.objects.filter(title='Галлерея').first().photos.all(),
            'menu': menu,
            'menucats': menucat,
            'menuitems': menuitem
        })
    else:
        return redirect('landing_page')
