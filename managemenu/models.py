from django.db import models

class FnB(models.Model):

    CATEGORIES = (
        ('Food', 'Food'),
        ('Beverage', 'Beverage')
    )

    name = models.CharField(max_length=20)
    price = models.IntegerField()
    category = models.CharField(null=True, max_length=15, choices=CATEGORIES)
    description = models.TextField(max_length=150, default='')
    fnbs = models.Manager()

    class Meta:
        db_table="fnb"

class Menu(models.Model):
    menu_id = models.CharField(max_length=30)
    foods = models.ForeignKey(FnB, on_delete=models.CASCADE, null=True)