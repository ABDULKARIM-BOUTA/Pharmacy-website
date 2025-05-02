from rest_framework import serializers
from medicine.models import Medicine, Category, Manufacturer

class MedicineSerializer(serializers.ModelSerializer):
    category = serializers.SlugRelatedField(queryset=Category.objects.all(), slug_field='name', required=False, allow_null=True)
    manufacturer = serializers.SlugRelatedField(queryset=Manufacturer.objects.all(), slug_field='name', required=False, allow_null=True)

    class Meta:
        model = Medicine
        fields = ['name', 'price', 'stock_quantity', 'description', 'dosage', 'requires_prescription', 'pk',
                  'weight_or_count', 'expiration_date', 'created_at', 'updated_at', 'category', 'manufacturer']