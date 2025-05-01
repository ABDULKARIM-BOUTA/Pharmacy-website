from django.urls import path
from medicine.views import MedicineCreateAPIView, MedicineListAPIView

app_name = 'medicine'

urlpatterns = [
    path('create/', MedicineCreateAPIView.as_view(), name='medicine-create'),
    path('list/', MedicineListAPIView.as_view(), name='medicine-list')
]