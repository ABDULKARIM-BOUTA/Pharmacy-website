from rest_framework.generics import CreateAPIView
from django.views.generic import TemplateView
from users.serializers import SignUpSerializer
from django.contrib.auth import get_user_model
from rest_framework.permissions import AllowAny
from rest_framework_simplejwt.views import TokenObtainPairView
from users.serializers import CustomTokenObtainPairSerializer
from django.views.decorators.csrf import csrf_exempt
from django.utils.decorators import method_decorator
from django.shortcuts import render

User = get_user_model()

class SignUpAPIView(CreateAPIView):
    permission_classes = [AllowAny]
    queryset = User.objects.all()
    serializer_class = SignUpSerializer

class SignUpPageView(TemplateView):
    template_name = 'users/signup.html'

@method_decorator(csrf_exempt, name='dispatch')
class CustomTokenObtainPairView(TokenObtainPairView):
    serializer_class = CustomTokenObtainPairSerializer

class LogInPageView(TemplateView):
    template_name = 'users/login.html'

def home(request):
    return render(request, 'home.html')