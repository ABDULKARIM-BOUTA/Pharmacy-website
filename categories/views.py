from categories.models import Category
from rest_framework.generics import ListAPIView, CreateAPIView, DestroyAPIView, RetrieveUpdateDestroyAPIView
from categories.serializers import CategorySerializer
from rest_framework.permissions import IsAdminUser
from django.views.generic import TemplateView

# API views
class CategoryListAPIView(ListAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    permission_classes = [IsAdminUser]

class CategoryCreateAPIView(CreateAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    permission_classes = [IsAdminUser]

class CategoryUpdateDeleteAPIView(RetrieveUpdateDestroyAPIView):
    lookup_field = 'pk'
    serializer_class = CategorySerializer
    queryset = Category.objects.all()
    permission_classes = [IsAdminUser]

# Templates Views
class CategoryListPageView(TemplateView):
    template_name = 'categories/list.html'

class CategoryCreatePageView(TemplateView):
    template_name = 'categories/create.html'

class CategoryUpdateDeletePageView(TemplateView):
    template_name = 'categories/update-delete.html'
