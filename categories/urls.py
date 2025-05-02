from django.urls import path
from categories import views

app_name = 'categories'

urlpatterns = [
    # api urls
    path('api/create/', views.CategoryCreateAPIView.as_view(), name='api-create'),
    path('api/list/', views.CategoryListAPIView.as_view(), name='api-list'),
    path('api/<int:pk>/update/', views.CategoryUpdateAPIView.as_view(), name='api-update'),
    path('api/<int:pk>/delete/', views.CategoryDeleteAPIView.as_view(), name='api-delete'),

    # templates urls
    path('create/', views.CategoryCreatePageView.as_view(), name='page-create'),
    path('list/', views.CategoryListPageView.as_view(), name='page-list'),
    path('<int:pk>/update/', views.CategoryUpdatePageView.as_view(), name='page-update'),
    path('<int:pk>/delete/', views.CategoryDeletePageView.as_view(), name='page-delete'),
]