from django.urls import path
from medicine import views

app_name = 'medicine'

urlpatterns = [
    # api urls
    path('api/create/', views.MedicineCreateAPIView.as_view(), name='medicine-api-create'),
    path('api/list/', views.MedicineListAPIView.as_view(), name='medicine-api-list'),
    path('api/<int:pk>/detail/', views.MedicineDetailAPIView.as_view(), name='medicine-api-detail'),
    path('api/<int:pk>/update/', views.MedicineUpdateAPIView.as_view(), name='medicine-api-update'),
    path('api/<int:pk>/delete/', views.MedicineDeleteAPIView.as_view(), name='medicine-api-delete'),

    # templates urls
    path('create/', views.MedicineCreatePageView.as_view(), name='medicine-page-create'),
    path('list/', views.MedicineListPageView.as_view(), name='medicine-page-list')
]