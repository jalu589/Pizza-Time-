# Generated by Django 4.1.1 on 2023-02-02 23:23

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("pizza", "0005_salad_alter_pizza_size_alter_pizza_title"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="pizza",
            name="flavor",
        ),
    ]
