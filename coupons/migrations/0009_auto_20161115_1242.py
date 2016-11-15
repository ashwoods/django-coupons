# -*- coding: utf-8 -*-
# Generated by Django 1.10.3 on 2016-11-15 12:42
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('coupons', '0008_auto_20161114_1546'),
    ]

    operations = [
        migrations.AddField(
            model_name='couponuser',
            name='reference',
            field=models.CharField(blank=True, max_length=150, verbose_name='Reference'),
        ),
        migrations.AlterUniqueTogether(
            name='couponuser',
            unique_together=set([]),
        ),
    ]
