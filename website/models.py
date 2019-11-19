from django.db import models
from django.utils import timezone
from django.urls import reverse
import datetime
CATEGORIES = (
    ('K', 'Kosulje'),
    ('P', 'Pantalone'),
    ('J', 'Jakne'),
    ('DZ', 'Dzemperi'),
    ('M', 'Majice'),
    ('T', 'Trenerke'),
    ('D', 'Duskevi'),
    ('A', 'Aksesoari')
)
COLORS = (
    ('R', 'red'),
    ('G', 'green'),
    ('B', 'blue'),
    ('Y', 'yellow'),
    ('G', 'green'),
    ('S', 'silver'),
    ('C', 'cyan'),
    ('BL', 'black'),
    ('W', 'white'),
    ('T', 'teal'),
    ('BG', 'beige')
)
SIZE_CHOICES = (
    ('XL', 'XL'),
    ('2XL', '2XL'),
    ('3XL', '3XL'),
    ('4XL', '4XL'),
    ('5XL', '5XL'),
    ('6XL', '6XL'),
    ('7XL', '7XL'),
    ('8XL', '8XL'),
    ('9XL', '9XL'),
    ('10XL', '10XL')
)

# Create your models here.


class Collection(models.Model):
    title = models.CharField(max_length=20, null=True, blank=True)

    def __str__(self):
        return self.title

        
class Color(models.Model):
    color = models.CharField(choices=COLORS, max_length=2)

    def __str__(self):
        return self.color
class Size(models.Model):
    size = models.CharField(choices=SIZE_CHOICES, max_length=4)

    def __str__(self):
        return self.size
class Product(models.Model):
    title = models.CharField(max_length=120)
    description = models.TextField()
    published_date = models.DateTimeField("published date", auto_now_add=True)
    category = models.CharField(choices=CATEGORIES, max_length=2)
    price = models.IntegerField()
    sale = models.BooleanField(default=False)
    popular = models.BooleanField(default=False)
    featured = models.BooleanField(default=False)
    discount = models.IntegerField(default=0)
    size = models.ManyToManyField(Size)
    chest = models.IntegerField()
    length = models.IntegerField()
    waist = models.IntegerField()
    colors = models.ManyToManyField(Color)
    image = models.FileField(upload_to='images/shop', null=True, blank=True)
    collection = models.ForeignKey(Collection, on_delete=models.CASCADE)
    def was_recently_published(self):
        now = timezone.now()
        return now - datetime.timedelta(days=3) <= self.published_date <= now
    def discount_price(self):
        difference = int((self.discount * self.price) / 100)
        return self.price - difference
    def __str__(self):
        return self.title
class Subscriber(models.Model):
    email = models.EmailField(max_length=256, unique=True)
    last_emailed_date = models.DateTimeField(null=True, blank=True)

    def __str__(self):
        return self.email

class Message(models.Model):
    email = models.EmailField(max_length=256)
    date = models.DateTimeField(auto_now_add=True)
    name = models.CharField(max_length=120)
    message = models.TextField()

    def __str(self):
        return self.name
