# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2019-07-11 19:04
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('userlogin', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='phonenumber',
            field=models.IntegerField(blank=True, max_length=11, null=True),
        ),
    ]
