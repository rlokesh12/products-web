# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2017-05-22 12:52
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0003_auto_20170522_1232'),
    ]

    operations = [
        migrations.AlterField(
            model_name='products',
            name='category',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='home.Category'),
        ),
    ]
