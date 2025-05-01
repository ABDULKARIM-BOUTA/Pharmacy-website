from django.urls import path
from users.views import SignUpAPIView, SignUpPageView

app_name = 'users'

urlpatterns = [
    path('signup/', SignUpPageView.as_view(), name='signup-page'),
    path('api/auth/signup/', SignUpAPIView.as_view(), name='signup-api'),
]