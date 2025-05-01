from django.urls import path
from users.views import SignUpAPIView, SignUpPageView, LogInAPIView, LogInPageView

app_name = 'users'

urlpatterns = [
    path('signup/', SignUpPageView.as_view(), name='signup-page'),
    path('api/auth/signup/', SignUpAPIView.as_view(), name='signup-api'),
    path('login/', LogInPageView.as_view(), name='login-page'),
    path('api/auth/login/', LogInAPIView.as_view(), name='login-api'),
]