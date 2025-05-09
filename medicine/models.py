from django.db import models
from categories.models import Category
from manufacturers.models import Manufacturer

class Medicine(models.Model):
    name = models.CharField(unique=True, max_length=250)
    price = models.FloatField()
    stock_quantity = models.IntegerField()
    description = models.TextField()
    dosage = models.CharField(max_length=200)
    requires_prescription = models.BooleanField(default=False)
    weight_or_count = models.CharField(max_length=100)  # Ex: 250ml, 12 tablets, 50g
    expiration_date = models.DateField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    category = models.ForeignKey(Category, on_delete=models.SET_NULL, related_name='category', null=True, blank=True)
    manufacturer = models.ForeignKey(Manufacturer, on_delete=models.SET_NULL, null=True, blank=True)

    def __str__(self):
        return self.name