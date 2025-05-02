from django.urls import path
from categories import views

app_name = 'categories'

urlpatterns = [
    # api urls
    path('api/create/', views.CategoryCreateAPIView.as_view(), name='api-create'),
    path('api/list/', views.CategoryListAPIView.as_view(), name='api-list'),
    path('api/<int:pk>/update-delete/', views.CategoryUpdateDeleteAPIView.as_view(), name='api-update-delete'),

    # templates urls
    path('create/', views.CategoryCreatePageView.as_view(), name='page-create'),
    path('list/', views.CategoryListPageView.as_view(), name='page-list'),
    path('<int:pk>/update-delete/', views.CategoryUpdateDeletePageView.as_view(), name='page-update-delete'),
]