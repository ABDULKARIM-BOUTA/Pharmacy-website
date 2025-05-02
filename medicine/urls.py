from django.urls import path
from medicine.views import MedicineCreateAPIView, MedicineListAPIView, MedicineDetailAPIView, MedicineUpdateAPIView, MedicineDeleteAPIView, MedicineCreatePageView

app_name = 'medicine'

urlpatterns = [
    # api urls
    path('api/create/', MedicineCreateAPIView.as_view(), name='medicine-api-create'),
    path('api/list/', MedicineListAPIView.as_view(), name='medicine-api-list'),
    path('api/<int:pk>/detail/', MedicineDetailAPIView.as_view(), name='medicine-api-detail'),
    path('api/<int:pk>/update/', MedicineUpdateAPIView.as_view(), name='medicine-api-update'),
    path('api/<int:pk>/delete/', MedicineDeleteAPIView.as_view(), name='medicine-api-delete'),

    # templates urls
    path('create/', MedicineCreatePageView.as_view(), name='medicine-page-create'),

]