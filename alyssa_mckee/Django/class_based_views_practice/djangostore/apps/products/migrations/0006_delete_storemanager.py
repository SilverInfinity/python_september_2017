# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2017-09-28 15:15
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0005_auto_20170927_1937'),
    ]

    operations = [
        migrations.DeleteModel(
            name='StoreManager',
        ),
    ]
