from rest_framework.generics import CreateAPIView, ListAPIView
from medicine.models import Medicine
from medicine.serializers import MedicineSerializer
from rest_framework.permissions import IsAdminUser, AllowAny

class MedicineCreateAPIView(IsAdminUser, CreateAPIView):
    queryset = Medicine.objects.all()
    serializer_class = MedicineSerializer

class MedicineListAPIView(AllowAny, ListAPIView):
    queryset = Medicine.objects.all()
    serializer_class = MedicineSerializer
