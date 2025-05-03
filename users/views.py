from rest_framework.generics import CreateAPIView
from django.views.generic import TemplateView
from django.views.decorators.csrf import csrf_exempt
from django.utils.decorators import method_decorator
from django.shortcuts import render
from users.serializers import SignUpSerializer
from django.contrib.auth import get_user_model
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework_simplejwt.views import TokenObtainPairView
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework.views import APIView
from rest_framework.response import Response
from users.serializers import CustomTokenObtainPairSerializer

User = get_user_model()

class SignUpAPIView(CreateAPIView):
    permission_classes = [AllowAny]
    queryset = User.objects.all()
    serializer_class = SignUpSerializer

class SignUpPageView(TemplateView):
    template_name = 'users/signup.html'

class LogoutAPIView(APIView):
    permission_classes = [IsAuthenticated]

    def post(self, request):
        try:
            refresh_token = request.data["refresh"]
            token = RefreshToken(refresh_token)
            token.blacklist()
            return Response({"detail": "Logout successful"})
        except Exception as e:
            return (Response({"error": str(e)}, status=400)

@method_decorator(csrf_exempt, name='dispatch'))
class CustomTokenObtainPairView(TokenObtainPairView):
    serializer_class = CustomTokenObtainPairSerializer

class LogInPageView(TemplateView):
    template_name = 'users/login.html'

def home(request):
    return render(request, 'home.html')