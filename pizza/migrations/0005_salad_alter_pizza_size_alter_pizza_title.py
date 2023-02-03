# Generated by Django 4.1.1 on 2023-02-02 23:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("pizza", "0004_alter_pizza_size"),
    ]

    operations = [
        migrations.CreateModel(
            name="Salad",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("title", models.CharField(max_length=32)),
                ("pic", models.ImageField(upload_to="")),
                ("description", models.TextField()),
                (
                    "size",
                    models.CharField(
                        blank=True,
                        choices=[("Small", "Small"), ("Large", "Large")],
                        max_length=16,
                    ),
                ),
            ],
        ),
        migrations.AlterField(
            model_name="pizza",
            name="size",
            field=models.CharField(
                blank=True,
                choices=[("Small", "Small"), ("Medium", "Medium"), ("Large", "Large")],
                max_length=16,
            ),
        ),
        migrations.AlterField(
            model_name="pizza",
            name="title",
            field=models.CharField(max_length=32),
        ),
    ]
