from django.urls import path
from .views import CartPageView, CartDetailAPIView, AddToCartAPIView

app_name = 'carts'

urlpatterns = [
    path('', CartPageView.as_view(), name='page-cart'),  # For the template view
    path('api/', CartDetailAPIView.as_view(), name='api-detail'),
    path('api/add/', AddToCartAPIView.as_view(), name='api-add-to-cart'),
]