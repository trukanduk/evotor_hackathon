# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2017-12-02 15:08
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='tags',
            field=models.ManyToManyField(null=True, related_name='_product_tags_+', to='shop.ProductTag'),
        ),
    ]
