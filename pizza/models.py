from django.contrib.auth.models import AbstractUser
from django.db import models
from model_utils import Choices

from multiselectfield import MultiSelectField


class User(AbstractUser):
    pass


class Order(models.Model):
    items = models.TextField()
    payment = models.BooleanField()
    delivery = models.BooleanField()
    address = models.TextField(blank=True)
    request = models.TextField(blank=True)
    orderee = models.ForeignKey("User", on_delete=models.CASCADE, related_name="orders")


class Pizza(models.Model):
    title = models.CharField(max_length=32)
    pic = models.ImageField()
    description = models.TextField()
    sizes = Choices("Small", "Medium", "Large")
    size = models.CharField(choices=sizes, max_length=16, blank=True)
    toppings = Choices("Extra Cheese", "Pepperoni", "Bacon", "Peppers", "Mushrooms", "Chicken", "Pesto", "Ranch", "Beef")
    extras = MultiSelectField(choices=toppings, max_choices=9, max_length=32, blank=True)

    PIZZA_PRICES = {
    "Small": {
        "Cheese": 7.99,
        "Pepperoni": 8.99,
        "Custom": 9.99
    },
    "Medium": {
        "Cheese": 10.99,
        "Pepperoni": 11.99,
        "Custom": 12.99
    },
    "Large": {
        "Cheese": 13.99,
        "Pepperoni": 14.99,
        "Custom": 15.99
    }}


class Salad(models.Model):
    title = models.CharField(max_length=32)
    pic = models.ImageField()
    description = models.TextField()
    sizes = Choices("Small", "Large")
    size = models.CharField(choices=sizes, max_length=16, blank=True)

    SALAD_PRICES = {
        "Small": 5.99,
        "Large": 9.99
    }


class Cookie(models.Model):
    title = models.CharField(max_length=32)
    pic = models.ImageField()
    description = models.TextField()

    COOKIE_PRICE = 1.99


class IceCream(models.Model):
    title = models.CharField(max_length=32)
    pic = models.ImageField()
    description = models.TextField()
    flavors = Choices("Vanilla", "Chocolate", "Strawberry")
    flavor = models.CharField(choices=flavors, max_length=16, blank=True)

    ICECREAM_PRICE = 3.99


class Beverage(models.Model):
    title = models.CharField(max_length=32)
    pic = models.ImageField()
    description = models.TextField()
    sizes = Choices("Individual", "2L")
    size = models.CharField(choices=sizes, max_length=16, blank=True)

    BEVERAGE_PRICE = {
        "Soda": {
            "Individual": 1.99,
            "2L": 3.99
        },
        "Beer": {
            "Individual": 3.99,
            "2L": 7.99
        }
    }