# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-02-10 21:36
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('AssetStorage', '0002_auto_20170209_1834'),
    ]

    operations = [
        migrations.AddField(
            model_name='asset',
            name='file',
            field=models.FileField(blank=True, null=True, upload_to='test_folder'),
        ),
    ]
