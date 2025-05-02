from django.urls import path
from medicine import views

app_name = 'medicine'

urlpatterns = [
    # api urls
    path('api/create/', views.MedicineCreateAPIView.as_view(), name='api-create'),
    path('api/list/', views.MedicineListAPIView.as_view(), name='api-list'),
    path('api/<int:pk>/detail/', views.MedicineDetailAPIView.as_view(), name='api-detail'),
    path('api/<int:pk>/update/', views.MedicineUpdateAPIView.as_view(), name='api-update'),
    path('api/<int:pk>/delete/', views.MedicineDeleteAPIView.as_view(), name='api-delete'),

    # templates urls
    path('create/', views.MedicineCreatePageView.as_view(), name='page-create'),
    path('list/', views.MedicineListPageView.as_view(), name='page-list'),
    path('<int:pk>/detail/', views.MedicineDetailPageView.as_view(), name='page-detail'),
    path('<int:pk>/update/', views.MedicineUpdatePageView.as_view(), name='page-update'),
]