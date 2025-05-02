from django.urls import path
from users.views import SignUpAPIView, SignUpPageView, CustomTokenObtainPairView, LogInAPIView, LogInPageView, home
from rest_framework_simplejwt.views import TokenRefreshView

app_name = 'users'

urlpatterns = [
    # frontend urls
    path('signup/', SignUpPageView.as_view(), name='signup-page'),   # Signup page
    path('login/', LogInPageView.as_view(), name='login-page'),       # Login page

    # backend urls
    path('api/auth/signup/', SignUpAPIView.as_view(), name='signup-api'),   # API for signup
    path('api/auth/login/', CustomTokenObtainPairView.as_view(), name='login-api'),  # API for login
    path('refresh/', TokenRefreshView.as_view(), name='token_refresh'),    # API for token refresh
    path('', home, name='home'),
]