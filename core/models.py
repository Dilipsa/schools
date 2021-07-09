from django.db import models
from django.contrib.auth.models import User
from embed_video.fields import EmbedVideoField
from django.core.validators import MinLengthValidator
import datetime
from django.contrib.auth.models import User
class Taker(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="user")
    first_name = models.CharField(max_length=20)
    last_name = models.CharField(max_length=20)
    email = models.EmailField(max_length=20)
    image = models.ImageField(upload_to="taker_image")
    video = EmbedVideoField()
    description = models.TextField()
    approve = models.BooleanField(default=False)

    def __str__(self):
        return self.user.username
    

class Volunteer(models.Model):
    volunteer_taker = models.ForeignKey(User, on_delete=models.CASCADE, related_name="volunteer_taker")
    volunteer_giver = models.ForeignKey(User, on_delete=models.CASCADE, related_name="volunteer_giver")
    donation_thing = models.TextField()
    approve = models.BooleanField(default=False)

    def __str__(self):
        return self.user.username

class Donate(models.Model):
    taker = models.ForeignKey(User, on_delete=models.CASCADE, related_name="taker")
    giver = models.ForeignKey(User, on_delete=models.CASCADE, related_name="giver")
    donation_amount = models.PositiveIntegerField()
    date = models.DateField(auto_now_add=True, null=True)
    donated = models.BooleanField(default=True)

    def __str__(self):
        return self.taker


class Feedback(models.Model):
    feedback_giver = models.ForeignKey(User, on_delete=models.CASCADE, related_name="feedback_giver")
    feedback_to = models.ForeignKey(User, on_delete=models.CASCADE, related_name="feedback_to")
    feedback = models.TextField()
    date = models.DateField(auto_now_add=True)
    publish = models.BooleanField(default=True)

    def __str__(self):
        return self.feedback_giver
    



class Product(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=20)
    price = models.IntegerField(default=0)
    description = models.CharField(max_length=200, null=True , blank=True)
    image = models.ImageField(upload_to='books')

    @staticmethod
    def get_books_by_id(ids):
        return Product.objects.filter(id__in =ids)

    @staticmethod
    def get_all_products():
        return Product.objects.all()

class Order(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    quantity = models.IntegerField(default=1)
    price = models.IntegerField()
    address = models.CharField(max_length=50, default='', blank=True)
    phone = models.CharField(max_length=50, default='', blank=True)
    date = models.DateField(default=datetime.datetime.today)
    status = models.BooleanField(default=False)

    def placeOrder(self):
        self.save()

    @staticmethod
    def get_orders_by_customer(customer_id):
        return Order.objects.filter(customer=customer_id).order_by('-date')

