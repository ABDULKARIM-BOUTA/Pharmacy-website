from manufacturers.models import Manufacturer
from rest_framework.generics import ListAPIView, CreateAPIView, RetrieveUpdateDestroyAPIView
from manufacturers.serializers import ManufacturerSerializer
from rest_framework.permissions import IsAdminUser
from django.views.generic import TemplateView
from django.contrib.auth.mixins import UserPassesTestMixin

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

class ManufacturerListPageView(UserPassesTestMixin, TemplateView):
    template_name = 'manufacturer/list.html'
    raise_exception = True

    def test_func(self):
        return self.request.user.is_superuser

class ManufacturerCreatePageView(UserPassesTestMixin, TemplateView):
    template_name = 'manufacturer/create.html'
    raise_exception = True

    def test_func(self):
        return self.request.user.is_superuser

class ManufacturerUpdateDeletePageView(UserPassesTestMixin, TemplateView):
    template_name = 'manufacturer/update-delete.html'
    raise_exception = True

    def test_func(self):
        return self.request.user.is_superuser