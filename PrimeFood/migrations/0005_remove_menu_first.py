# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-02-11 01:27
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('PrimeFood', '0004_menu_first'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='menu',
            name='first',
        ),
    ]
