from django.urls import path
from users.views import SignUpAPIView, SignUpPageView, CustomTokenObtainPairView, LogInPageView, LogoutAPIView
from rest_framework_simplejwt.views import TokenRefreshView

app_name = 'users'

urlpatterns = [
    # frontend urls
    path('signup/', SignUpPageView.as_view(), name='signup-page'),
    path('login/', LogInPageView.as_view(), name='login-page'),
    path('logout/', LogoutAPIView.as_view(), name='logout-page'),

    # backend urls
    path('api/auth/signup/', SignUpAPIView.as_view(), name='signup-api'),
    path('api/auth/login/', CustomTokenObtainPairView.as_view(), name='login-api'),
    path('refresh/', TokenRefreshView.as_view(), name='token_refresh'),
]