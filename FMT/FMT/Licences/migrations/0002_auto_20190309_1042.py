# -*- coding: utf-8 -*-
# Generated by Django 1.11.18 on 2019-03-09 09:42
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Licences', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='UserManager',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
        ),
        migrations.AddField(
            model_name='licences',
            name='licence_number',
            field=models.CharField(default=0, max_length=255),
        ),
    ]
