from django.db import models
from django.contrib.auth.models import User
import uuid
from django.utils import timezone

class Driver(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    avatar = models.ImageField(upload_to='driver/avatar/', blank=True, null=True)
    phone_number = models.CharField(max_length=12, blank=True)
    earnings = models.FloatField(default=0.0)

    def __str__(self) -> str:
        return self.user.get_full_name()

class Customer(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    avatar = models.ImageField(upload_to='customer/avatar/', blank=True, null=True)
    phone_number = models.CharField(max_length=12, blank=True)
    adress = models.CharField(max_length=100, blank=True)

    def __str__(self) -> str:
        return self.user.get_full_name()
    
class Category(models.Model):
    slug = models.CharField(max_length=255, unique=True)
    name = models.CharField(max_length=255)

    def __str__(self) -> str:
        return self.name

class Order(models.Model):
    SMALL_SIZE = 'small'
    MEDIUM_SIZE = 'medium'
    LARGE_SIZE = 'large'
    SIZES = (
        (SMALL_SIZE, 'Small'),
        (MEDIUM_SIZE, 'Medium'),
        (LARGE_SIZE, 'Large'),
    )

    CREATING_STATUS = 'creating'
    PROCESSING_STATUS = 'processing'
    PICKING_STATUS = 'picking'
    DELIVERY_STATUS = 'delivery'
    COMPLETED_STATUS = 'completed'
    CANCELED_STATUS = 'canceled'
    STATUS = (
        (CREATING_STATUS, 'Creating'),
        (PROCESSING_STATUS, 'Processing'),
        (PICKING_STATUS, 'Picking'),
        (DELIVERY_STATUS, 'Delivery'),
        (COMPLETED_STATUS, 'Completed'),
        (CANCELED_STATUS, 'Canceled'),
    )

    # Step 1
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)
    driver = models.ForeignKey(Driver, on_delete=models.CASCADE, null=True, blank=True)
    name = models.CharField(max_length=255)
    description = models.CharField(max_length=255)
    category = models.ForeignKey(Category, on_delete=models.SET_NULL, null=True, blank=True)
    size = models.CharField(max_length=20, choices=SIZES, default=SMALL_SIZE)
    quantity = models.IntegerField(default=1)
    photo = models.ImageField(upload_to='order/photos/')
    status = models.CharField(max_length=20, choices=STATUS, default=CREATING_STATUS)
    create_at = models.DateField(default=timezone.now)

    # Step 2
    pickup_adress = models.CharField(max_length=255, blank=True)
    pickup_name = models.CharField(max_length=255, blank=True)
    pickup_phone = models.CharField(max_length=12, blank=True)

    # Step 3
    delivery_address = models.CharField(max_length=255, blank=True)
    delivery_name = models.CharField(max_length=255, blank=True)
    delivery_phone = models.CharField(max_length=12, blank=True)

    # Step 4
    CARD_PAYMENT = 'card payment'
    CASH_PAYMENT = 'cash payment'
    PAYMENT = (
        (CARD_PAYMENT, 'Card Payment'),
        (CASH_PAYMENT, 'Cash Payment')
    )
    payment_methods = models.CharField(max_length=50, choices=PAYMENT, default=CASH_PAYMENT)
    price = models.FloatField(default=15000.0)

    def __str__(self):
        return self.name
