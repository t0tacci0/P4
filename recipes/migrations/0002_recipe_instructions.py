# Generated by Django 5.0.6 on 2024-06-11 22:27

import djrichtextfield.models
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("recipes", "0001_initial"),
    ]

    operations = [
        migrations.AddField(
            model_name="recipe",
            name="instructions",
            field=djrichtextfield.models.RichTextField(
                default="No instructions available", max_length=10000
            ),
            preserve_default=False,
        ),
    ]
