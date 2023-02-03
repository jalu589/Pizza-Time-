# Generated by Django 4.1.1 on 2023-01-31 01:41

from django.db import migrations
import multiselectfield.db.fields


class Migration(migrations.Migration):

    dependencies = [
        ("pizza", "0002_pizza"),
    ]

    operations = [
        migrations.AlterField(
            model_name="pizza",
            name="extras",
            field=multiselectfield.db.fields.MultiSelectField(
                blank=True,
                choices=[
                    ("Extra Cheese", "Extra Cheese"),
                    ("Pepperoni", "Pepperoni"),
                    ("Bacon", "Bacon"),
                    ("Peppers", "Peppers"),
                    ("Mushrooms", "Mushrooms"),
                    ("Chicken", "Chicken"),
                    ("Pesto", "Pesto"),
                    ("Ranch", "Ranch"),
                    ("Beef", "Beef"),
                ],
                max_length=32,
            ),
        ),
    ]