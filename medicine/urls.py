from django.urls import path
from medicine.views import MedicineCreateAPIView, MedicineListAPIView, MedicineDetailAPIView, MedicineUpdateAPIView, MedicineDeleteAPIView

app_name = 'medicine'

urlpatterns = [
    path('create/', MedicineCreateAPIView.as_view(), name='medicine-create'),
    path('list/', MedicineListAPIView.as_view(), name='medicine-list'),
    path('<int:pk>/detail/', MedicineDetailAPIView.as_view(), name='medicine-detail'),
    path('<int:pk>/update/', MedicineUpdateAPIView.as_view(), name='medicine-update'),
    path('<int:pk>/delete/', MedicineDeleteAPIView.as_view(), name='medicine-delete'),
]