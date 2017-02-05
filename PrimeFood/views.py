from django.shortcuts import render, redirect
from django.forms.models import model_to_dict
from photologue.models import Gallery
from .models import *
import datetime
from django.contrib.auth import views as auth_views


def landing_page(request):
    menu = Menu.objects.all().order_by('order')
    menucat = MenuCategory.objects.all().order_by('order')
    menuitem = MenuItem.objects.all().order_by('order')
    menudata = dict((m.title, {mc.title: {'id': mc.id, 'items':[model_to_dict(mi) for mi in menuitem if mi.menucategory == mc and mi.menucategory.menu == m]} for mc in menucat if mc.menu == m}) for m in menu)
    for m in menu:
        menudata[m.title].update({'id': m.id})
    sd = request.META['HTTP_HOST'].split(".")
    if sd[0] == 'demo' or sd[1] == 'demo':
        if request.user.is_authenticated():
            return render(request, 'landing_page.html', {
                'title': 'PrimeFood DEMO',
                'slidergallery': Gallery.objects.filter(title='Слайдер').first().photos.all(),
                'gallery': Gallery.objects.filter(title='Галлерея').first().photos.all(),
                'menudata': menudata
            })
        else:
            redirect(auth_views.login)
    elif datetime.date.today() < datetime.date(2017, 2, 9):
        return render(request, 'timer.html', {
            'start_date': str(datetime.date(2017, 2, 9).strftime('%Y/%m/%d')),
            'title': 'PrimeFood'
        })
    else:
        return render(request, 'landing_page.html', {
            'title': "PrimeFood",
            'slidergallery': Gallery.objects.filter(title='Слайдер').first().photos.all(),
            'gallery': Gallery.objects.filter(title='Галлерея').first().photos.all(),
            'menudata': menudata
        })
