from django.urls import path
from manufacturers import views

app_name = 'manufacturers'

urlpatterns = [
    # api urls
    path('api/create/', views.ManufacturerCreateAPIView.as_view(), name='api-create'),
    path('api/list/', views.ManufacturerListAPIView.as_view(), name='api-list'),
    path('api/<int:pk>/update-delete/', views.ManufacturerUpdateDeleteAPIView.as_view(), name='api-update-delete'),

    # templates urls
    path('create/', views.ManufacturerCreatePageView.as_view(), name='page-create'),
    path('list/', views.ManufacturerListPageView.as_view(), name='page-list'),
    path('<int:pk>/update-delete/', views.ManufacturerUpdateDeletePageView.as_view(), name='page-update-delete'),
]