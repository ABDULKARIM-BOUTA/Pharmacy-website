from orders.models import Order, OrderItem
from rest_framework import serializers
from medicine.serializers import MedicineSerializer
from medicine.models import Medicine
from users.models import User

class OrderItemSerializer(serializers.ModelSerializer):
    medicine = MedicineSerializer(read_only=True)
    medicine_id = serializers.PrimaryKeyRelatedField(queryset=Medicine.objects.all(), source='medicine', write_only=True)

    class Meta:
        model = OrderItem
        fields = ['order', 'medicine', 'price', 'quantity', 'total_price', 'medicine_id' ]
        read_only_fields = ['price', 'total_price']

class OrderSerializer(serializers.ModelSerializer):
    items = OrderItemSerializer(many=True)
    user = serializers.StringRelatedField(read_only=True)
    user_id = serializers.PrimaryKeyRelatedField(queryset=User.objects.all(), source='user', write_only=True, required=False)

    class Meta:
        model = Order
        fields = ['id', 'items', 'user', 'user_id', 'address', 'created_at',
                  'update_at', 'status', 'total_amount', 'payment_method']

        read_only_fields = ['created_at', 'updated_at', 'total_amount']

    def create(self, validated_data):
        items_data = validated_data.pop('items')
        order = Order.objects.create(**validated_data)

        total_amount = 0
        for item_data in items_data:
            medicine = item_data['medicine']
            quantity = item_data['quantity']
            price = medicine.price  # Get current price from medicine

            OrderItem.objects.create(
                order=order,
                medicine=medicine,
                quantity=quantity,
                price=price
            )
            total_amount += quantity * price

        order.total_amount = total_amount
        order.save()
        return order