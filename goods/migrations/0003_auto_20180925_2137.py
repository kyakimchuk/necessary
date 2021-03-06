# -*- coding: utf-8 -*-
# Generated by Django 1.11.15 on 2018-09-25 18:37
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('goods', '0002_auto_20180925_2001'),
    ]

    operations = [
        migrations.CreateModel(
            name='Category2',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=60, verbose_name='Название')),
            ],
            options={
                'verbose_name': 'Категория2',
                'verbose_name_plural': 'Категории2',
            },
        ),
        migrations.CreateModel(
            name='Category3',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=60, verbose_name='Название')),
            ],
            options={
                'verbose_name': 'Категория3',
                'verbose_name_plural': 'Категории3',
            },
        ),
        migrations.CreateModel(
            name='CategoryHierarchy',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
            options={
                'verbose_name': 'Иерархия категорий',
                'verbose_name_plural': 'Иерархии категорий',
            },
        ),
        migrations.CreateModel(
            name='Thing',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=60, verbose_name='Название')),
                ('description', models.TextField(verbose_name='Описание')),
                ('price', models.IntegerField(verbose_name='Цена')),
                ('size', models.CharField(max_length=15, verbose_name='Размер')),
                ('cat_hierar', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='goods.CategoryHierarchy', verbose_name='Иерархия категорий')),
            ],
            options={
                'verbose_name': 'Вещь',
                'verbose_name_plural': 'Вещи',
            },
        ),
        migrations.AlterField(
            model_name='category1',
            name='name',
            field=models.CharField(max_length=60, verbose_name='Название'),
        ),
        migrations.AddField(
            model_name='categoryhierarchy',
            name='cat1',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='goods.Category1', verbose_name='Категория1'),
        ),
        migrations.AddField(
            model_name='categoryhierarchy',
            name='cat2',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='goods.Category2', verbose_name='Категория2'),
        ),
        migrations.AddField(
            model_name='categoryhierarchy',
            name='cat3',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='goods.Category3', verbose_name='Категория3'),
        ),
    ]
