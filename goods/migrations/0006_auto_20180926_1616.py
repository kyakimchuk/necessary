# -*- coding: utf-8 -*-
# Generated by Django 1.11.15 on 2018-09-26 13:16
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('goods', '0005_thing_photo1'),
    ]

    operations = [
        migrations.AlterField(
            model_name='thing',
            name='description',
            field=models.TextField(blank=True, null=True, verbose_name='Описание'),
        ),
        migrations.AlterField(
            model_name='thing',
            name='size',
            field=models.CharField(blank=True, max_length=15, null=True, verbose_name='Размер'),
        ),
    ]
