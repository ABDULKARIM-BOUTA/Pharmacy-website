from rest_framework import serializers
from medicine.models import Medicine

class MedicineSerializer(serializers.ModelSerializer):
    category = serializers.StringRelatedField()
    manufacturer = serializers.StringRelatedField()

    class Meta:
        model = Medicine
        fields = ['name', 'price', 'stock_quantity', 'description', 'dosage', 'requires_prescription', 'pk',
                  'weight_or_count', 'expiration_date', 'created_at', 'updated_at', 'category', 'manufacturer']