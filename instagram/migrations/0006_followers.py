# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2019-05-23 07:21
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('instagram', '0005_photolikes'),
    ]

    operations = [
        migrations.CreateModel(
            name='Followers',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user', models.CharField(default='', max_length=20)),
                ('follower', models.CharField(default='', max_length=20)),
            ],
        ),
    ]