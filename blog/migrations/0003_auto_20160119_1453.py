# -*- coding: utf-8 -*-
# Generated by Django 1.9.1 on 2016-01-19 12:53
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0002_auto_20160115_1135'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='article',
            options={'ordering': ['-created']},
        ),
        migrations.RenameField(
            model_name='article',
            old_name='cheated',
            new_name='created',
        ),
    ]
