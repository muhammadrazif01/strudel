from django.db import models

# Create your models here.
class Order(models.Model):
    reservation = models.ForeignKey('Reservation', on_delete=models.CASCADE, null=True) #ManyToOne relationship with Reservation, also deletes Order if referenced Reservation is deleted
    total_price = models.IntegerField()
    payment_method = models.CharField(max_length=100)
    status = models.CharField(max_length=100) # ["waiting for payment", "successful "]
    orders = models.Manager()

class FnbChoice(models.Model):
    order = models.ForeignKey('Order', default=None,  on_delete=models.CASCADE, null=True) #ManyToOne relationship with Order, also deletes FnbChoice if referenced Order is deleted
    fnb = models.ForeignKey('Fnb', on_delete=models.CASCADE)
    amount = models.IntegerField()
    fnbchoices = models.Manager()
    def __str__(self):
        return "{:<8}".format(str(self.amount)+" x") + "{:<50}".format(str(self.fnb)) + "Rp.{:>15}".format(self.fnb.get("price") * self.amount)

# move to managemenu app
class Menu(models.Model):
    fnb = models.ManyToManyField('Fnb')
    restaurant = models.OneToOneField('Restaurant', on_delete=models.CASCADE, null=True) #OneToOne relationship with Restaurant, also deletes Menu if referenced Restaurant is deleted
    menus = models.Manager()
    def __str__(self):
        return "Menu of " + str(self.restaurant)

# move to managemenu app
class Fnb(models.Model):
    name = models.CharField(max_length=100)
    price = models.IntegerField()
    fnbs = models.Manager()
    def __str__(self):
        return self.name

class Restaurant(models.Model):
    name = models.CharField(max_length=100)
    restaurants = models.Manager()
    def __str__(self):
        return self.name

# move to reservation app
class Reservation(models.Model):
    restaurant = models.ForeignKey('Restaurant', on_delete=models.CASCADE, null=True) #ManyToOne relationship with Restaurant, also deletes Reservation if referenced Restaurant is deleted
    reservations = models.Manager()
    def __str__(self):
        return "Reservation at " + str(self.restaurant)