# Generated by Django 4.1.1 on 2022-10-27 14:44

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("website", "0005_post"),
    ]

    operations = [
        migrations.DeleteModel(name="Post",),
    ]
