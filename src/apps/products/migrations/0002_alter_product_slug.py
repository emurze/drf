# Generated by Django 5.0.6 on 2024-07-06 06:06

import autoslug.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("products", "0001_initial"),
    ]

    operations = [
        migrations.AlterField(
            model_name="product",
            name="slug",
            field=autoslug.fields.AutoSlugField(
                editable=False, populate_from="title", unique=True
            ),
        ),
    ]
