# -*- coding: utf-8 -*-
# Generated by Django 1.9.7 on 2016-11-17 11:39
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('asset', '0005_gobuild'),
    ]

    operations = [
        migrations.CreateModel(
            name='gostatus',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('supervisor_host', models.CharField(default=b'192.168.1.1', max_length=128)),
                ('supervisor_username', models.CharField(max_length=64)),
                ('supervisor_password', models.CharField(max_length=64)),
                ('supervisor_port', models.CharField(default=b'9001', max_length=128)),
                ('hostname', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='asset.minion')),
            ],
        ),
    ]