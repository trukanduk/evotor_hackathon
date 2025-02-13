# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2017-12-02 21:35
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('shop', '0008_shop'),
    ]

    operations = [
        migrations.CreateModel(
            name='UserShop',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('type', models.CharField(choices=[('r', 'Read'), ('rw', 'Read/Write')], default='rw', max_length=2)),
                ('shop', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='+', to='shop.Shop')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='+', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
