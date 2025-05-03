from django.db import models
from django.contrib.auth import get_user_model
from medicine.models import Medicine
from django.core.validators import MinValueValidator

User = get_user_model()

class Order(models.Model):
    STATUS_CHOICES = [
        ('pending', 'Pending'),
        ('completed', 'Completed'),
        ('cancelled','Cancelled')
    ]

    PAYMENT_CHOICES = [
        ('cash', 'Cash On Delivery'),
        ('credit', 'Credit Card On Delivery')
    ]

    user = models.ForeignKey(User, on_delete=models.CASCADE)
    address = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    status = models.CharField(choices=STATUS_CHOICES, default='pending', max_length=20)
    total_amount = models.DecimalField(max_digits=10, decimal_places=2, default=0.00, validators=[MinValueValidator(0)])
    payment_method = models.CharField(max_length=50, choices=PAYMENT_CHOICES, default=None)

    class Meta:
        ordering = ['-created_at']

    def __str__(self):
        return f'#Order{self.id}: {self.user}'


class OrderItem(models.Model):
    order = models.ForeignKey(Order, on_delete=models.CASCADE)
    medicine = models.ForeignKey(Medicine, on_delete=models.PROTECT)
    quantity = models.PositiveIntegerField(validators=[MinValueValidator(1)])
    price = models.DecimalField(max_digits=10, decimal_places=2, default=0.00, validators=[MinValueValidator(0)])

    @property
    def total_price(self):
        return self.price * self.quantity

    def __str__(self):
        return f' #Order: {self.order.id} (Price: {self.price} x Quantity: {self.quantity})'