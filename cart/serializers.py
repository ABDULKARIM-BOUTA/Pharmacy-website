from cart.models import CartItem, Cart
from rest_framework import serializers
from medicine.serializers import MedicineSerializer

class CartItemSerializer(serializers.ModelSerializer):
    medicine = MedicineSerializer()
    total_price = serializers.SerializerMethodField()

    class Meta:
        model = CartItem
        fields = ['id', 'medicine', 'quantity', 'total_price']

    def get_total_price(self, obj):
        return obj.total_price

class CartSerializer(serializers.ModelSerializer):
    items = CartItemSerializer(many=True, read_only=True)
    total_price = serializers.SerializerMethodField()

    class Meta:
        model = Cart
        fields = ['id', 'items', 'total_price']

    def get_total_price(self, obj):
        return obj.total_price
