# Generated by Django 4.1.1 on 2022-10-22 14:38

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("website", "0002_listing_image"),
    ]

    operations = [
        migrations.RemoveField(model_name="listing", name="num_bathrooms",),
        migrations.RemoveField(model_name="listing", name="num_bedrooms",),
        migrations.RemoveField(model_name="listing", name="price",),
        migrations.RemoveField(model_name="listing", name="square_footage",),
    ]
