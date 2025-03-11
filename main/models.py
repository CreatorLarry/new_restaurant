from django.db import models

# Create your models here.
CATEGORY_CHOICES = [
    ('fast-food', 'Fast food'),
    ('appetizers', 'Appetizers'),
    ('main-course', 'Main Course'),
    ('desserts', 'Desserts'),
    ('drinks', 'Drinks'),
]


class Dish(models.Model):
    name = models.CharField(max_length=200)
    description = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    image = models.ImageField(upload_to='dishes/')
    category = models.CharField(max_length=50, choices=CATEGORY_CHOICES)

    def __str__(self):
        return self.name


class Reservation(models.Model):
    name = models.CharField(max_length=200)
    email = models.EmailField()
    phone = models.CharField(max_length=20, blank=True, null=True)
    date = models.DateField()
    time = models.TimeField()
    guest = models.PositiveIntegerField()
    message = models.TextField(blank=True, null=True)
    status = models.CharField(max_length=20,
                              choices=[('pending', 'Pending'), ('confirmed', 'Confirmed'), ('cancelled', 'Cancelled')])

    def __str__(self):
        return f"{self.name} - {self.date}"

class Order(models.Model):
    name = models.CharField(max_length=200)
    email = models.EmailField()
    phone = models.IntegerField()
    food_item = models.TextField()
    quantity = models.PositiveIntegerField()
    delivery_address = models.TextField()
    message = models.TextField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Order from {self.name} - {self.food_item}"