from categories.models import Category
from rest_framework.generics import ListAPIView, CreateAPIView, DestroyAPIView, RetrieveUpdateAPIView
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

class CategoryUpdateAPIView(RetrieveUpdateAPIView):
    lookup_field = 'pk'
    serializer_class = CategorySerializer
    queryset = Category.objects.all()
    permission_classes = [IsAdminUser]

class CategoryDeleteAPIView(DestroyAPIView):
    lookup_field = 'pk'
    serializer_class = CategorySerializer
    queryset = Category.objects.all()
    permission_classes = [IsAdminUser]

# Templates Views
class CategoryListPageView(TemplateView):
    template_name = 'categories/list.html'

class CategoryCreatePageView(TemplateView):
    template_name = 'categories/create.html'

class CategoryUpdatePageView(TemplateView):
    template_name = 'categories/Update.html'

class CategoryDeletePageView(TemplateView):
    template_name = 'categories/Delete.html'