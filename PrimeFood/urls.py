"""tula URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.10/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url, include
from django.conf.urls.static import static
from django.contrib import admin
from django.contrib.auth.views import logout

import PrimeFood.settings as settings
from . import views as myviews

urlpatterns = [
    url(r'^grappelli/', include('grappelli.urls')),
    url(r'^admin/logout/$', logout, {'next_page': 'http://prime-food.ru'}),
    url(r'^admin/', admin.site.urls),
    url(r'^photologue/', include('photologue.urls', namespace='photologue')),
    url(r'^demo/$', myviews.demo, name='demo'),
    url(r'^$', myviews.landing_page, name='landing_page'),
]
if settings.DEBUG is True:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
