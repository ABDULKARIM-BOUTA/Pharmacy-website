from rest_framework.generics import CreateAPIView
from django.views.generic import TemplateView
from users.serializers import SignUpSerializer
from django.contrib.auth import get_user_model
from rest_framework.permissions import AllowAny

User = get_user_model()

class SignUpAPIView(CreateAPIView):
    permission_classes = [AllowAny]
    queryset = User.objects.all()
    serializer_class = SignUpSerializer

class SignUpPageView(TemplateView):
    template_name = 'users/signup.html'