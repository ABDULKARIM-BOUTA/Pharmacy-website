from rest_framework.generics import CreateAPIView, ListAPIView, RetrieveAPIView, RetrieveUpdateAPIView, RetrieveDestroyAPIView, UpdateAPIView, DestroyAPIView
from medicine.models import Medicine
from medicine.serializers import MedicineSerializer
from rest_framework.permissions import IsAdminUser, AllowAny
from django.views.generic import TemplateView
from django.contrib.auth.mixins import UserPassesTestMixin

"""API views"""
class MedicineCreateAPIView(CreateAPIView):
    queryset = Medicine.objects.all()
    serializer_class = MedicineSerializer
    permission_classes = [IsAdminUser]

class MedicineListAPIView(ListAPIView):
    queryset = Medicine.objects.all()
    serializer_class = MedicineSerializer
    permission_classes = [AllowAny]

class MedicineDetailAPIView(RetrieveAPIView):
    lookup_field = 'pk'
    serializer_class = MedicineSerializer
    queryset = Medicine.objects.all()
    permission_classes = [AllowAny]

class MedicineUpdateAPIView(RetrieveUpdateAPIView):
    serializer_class = MedicineSerializer
    lookup_field = 'pk'
    queryset = Medicine.objects.all()
    permission_classes = [IsAdminUser]

class MedicineDeleteAPIView(DestroyAPIView):
    lookup_field = 'pk'
    serializer_class = MedicineSerializer
    queryset = Medicine.objects.all()
    permission_classes = [IsAdminUser]

#------------------------------------------------

"""Templates views"""

class MedicineListPageView(TemplateView):
    template_name = 'medicine/list.html'

class MedicineDetailPageView(TemplateView):
    template_name = 'medicine/detail.html'

class MedicineCreatePageView(UserPassesTestMixin, TemplateView):
    template_name = 'medicine/create.html'
    raise_exception = True

    def test_func(self):
        return self.request.user.is_superuser

class MedicineUpdatePageView(UserPassesTestMixin, TemplateView):
    template_name = 'medicine/update.html'
    raise_exception = True

    def test_func(self):
        return self.request.user.is_superuser