from rest_framework import generics
from .models import Order
from .serializers import OrderSerializer
from django.views.generic import TemplateView
from users.permissions import IsOwnerOrAdmin
from rest_framework.permissions import IsAuthenticated

class OrderListCreateAPIView(generics.ListCreateAPIView):
    serializer_class = OrderSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        if self.request.user.is_staff:
            return Order.objects.all()
        return Order.objects.filter(user=self.request.user)

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)

class OrderRetrieveUpdateDestroyAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer
    permission_classes = [IsOwnerOrAdmin]

    def perform_update(self, serializer):
        instance = serializer.save()
        # Recalculate total_amount if items change
        if 'items' in serializer.validated_data:
            total = sum(item.quantity * item.price for item in instance.items.all())
            instance.total_amount = total
            instance.save()

# Template views
class OrderListPageView(TemplateView):
    template_name = 'orders/list.html'

class OrderDetailPageView(TemplateView):
    template_name = 'orders/detail.html'

class CheckoutPageView(TemplateView):
    template_name = 'orders/checkout.html'