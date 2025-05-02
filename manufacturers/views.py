from manufacturers.models import Manufacturer
from rest_framework.generics import ListAPIView, CreateAPIView, RetrieveUpdateDestroyAPIView
from manufacturers.serializers import ManufacturerSerializer
from rest_framework.permissions import IsAdminUser
from django.views.generic import TemplateView

# API views
class ManufacturerListAPIView(ListAPIView):
    queryset = Manufacturer.objects.all()
    serializer_class = ManufacturerSerializer
    permission_classes = [IsAdminUser]

class ManufacturerCreateAPIView(CreateAPIView):
    queryset = Manufacturer.objects.all()
    serializer_class = ManufacturerSerializer
    permission_classes = [IsAdminUser]

class ManufacturerUpdateDeleteAPIView(RetrieveUpdateDestroyAPIView):
    lookup_field = 'pk'
    serializer_class = ManufacturerSerializer
    queryset = Manufacturer.objects.all()
    permission_classes = [IsAdminUser]

# Templates Views
class ManufacturerListPageView(TemplateView):
    template_name = 'manufacturer/list.html'

class ManufacturerCreatePageView(TemplateView):
    template_name = 'manufacturer/create.html'

class ManufacturerUpdateDeletePageView(TemplateView):
    template_name = 'manufacturer/update-delete.html'