from rest_framework.generics import CreateAPIView
from django.views.generic import TemplateView
from rest_framework.views import APIView
from users.serializers import SignUpSerializer, LogInSerializer
from django.contrib.auth import get_user_model
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from rest_framework import status

User = get_user_model()

class SignUpAPIView(CreateAPIView):
    permission_classes = [AllowAny]
    queryset = User.objects.all()
    serializer_class = SignUpSerializer

class SignUpPageView(TemplateView):
    template_name = 'users/signup.html'

class LogInAPIView(APIView):
    permission_classes = [AllowAny]

    def post(self, request, *args, **kwargs):
        serializer = LogInSerializer(data=request.data)
        if serializer.is_valid():
            return Response(serializer.validated_data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class LogInPageView(TemplateView):
    template_name = 'users/login.html'