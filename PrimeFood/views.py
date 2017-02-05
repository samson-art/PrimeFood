from django.shortcuts import render
from django.forms.models import model_to_dict
from photologue.models import Gallery
from .models import *
import datetime
from django.contrib.sites.models import Site


def landing_page(request):
    menu = Menu.objects.all().order_by('order')
    menucat = MenuCategory.objects.all().order_by('order')
    menuitem = MenuItem.objects.all().order_by('order')
    menudata = dict((m.title, {mc.title: {'id': mc.id, 'items':[model_to_dict(mi) for mi in menuitem if mi.menucategory == mc and mi.menucategory.menu == m]} for mc in menucat if mc.menu == m}) for m in menu)
    for m in menu:
        menudata[m.title].update({'id': m.id})

    django_site = Site.objects.get_current()
    host = request.META['HTTP_HOST']
    domain_parts = django_site.domain.split(".")
    domain = ".".join(domain_parts[1:])
    subdomain = request.META['HTTP_HOST'].replace(domain, '').replace('.', '').replace('www', '')
    if host == django_site.domain:
        return render(request, 'landing_page.html', {
            'title': 'PrimeFood DEMO',
            'slidergallery': Gallery.objects.filter(title='Слайдер').first().photos.all(),
            'gallery': Gallery.objects.filter(title='Галлерея').first().photos.all(),
            'menudata': menudata,
            'host': host,
            'domain': subdomain
        })
    if datetime.date.today() < datetime.date(2017, 2, 9):
        return render(request, 'timer.html', {
            'start_date': str(datetime.date(2017, 2, 9).strftime('%Y/%m/%d')),
            'title': 'PrimeFood',
            'host': host,
            'domain': subdomain
        })
    else:
        return render(request, 'landing_page.html', {
            'title': "PrimeFood",
            'slidergallery': Gallery.objects.filter(title='Слайдер').first().photos.all(),
            'gallery': Gallery.objects.filter(title='Галлерея').first().photos.all(),
            'menudata': menudata,
            'domain': subdomain
        })
