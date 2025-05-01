from rest_framework.generics import CreateAPIView
from django.views.generic import TemplateView
from users.serializers import SignUpSerializer
from django.contrib.auth import get_user_model
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt
from rest_framework.permissions import AllowAny

User = get_user_model()

@method_decorator(csrf_exempt, name='dispatch')
class SignUpAPIView(CreateAPIView):
    permission_classes = [AllowAny]
    queryset = User.objects.all()
    serializer_class = SignUpSerializer

class SignUpPageView(TemplateView):
    template_name = 'users/signup.html'