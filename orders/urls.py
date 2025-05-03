from django.urls import path
from orders import views

app_name = 'orders'

urlpatterns = [
    # API Endpoints
    path('api/', views.OrderListCreateAPIView.as_view(), name='api-list-create'),
    path('api/<int:pk>/', views.OrderRetrieveUpdateDestroyAPIView.as_view(), name='api-detail'),

    # Template Views
    path('', views.OrderListPageView.as_view(), name='page-list'),
    path('<int:pk>/', views.OrderDetailPageView.as_view(), name='page-detail'),
    path('checkout/', views.CheckoutPageView.as_view(), name='checkout'),
]