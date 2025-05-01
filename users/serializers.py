from rest_framework import serializers
from django.contrib.auth import get_user_model, authenticate
from rest_framework_simplejwt.tokens import RefreshToken

User = get_user_model()

class SignUpSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)

    class Meta:
        model = User
        fields = ['username', 'email', 'password']

    def create(self, validated_data):
        user = User.objects.create_user(
            email=validated_data['email'],
            username=validated_data['username'],
            password=validated_data['password']
        )
        return user

from rest_framework import serializers
from django.contrib.auth import authenticate, get_user_model
from rest_framework_simplejwt.tokens import RefreshToken

User = get_user_model()

class LogInSerializer(serializers.Serializer):
    username_or_email = serializers.CharField(required=True)
    password = serializers.CharField(
        required=True,
        write_only=True,
        style={'input_type': 'password'}
    )

    def validate(self, attrs):
        username_or_email = attrs.get('username_or_email')
        password = attrs.get('password')

        user = None

        # Try authenticating using username
        user = authenticate(username=attrs['username_or_email'], password=attrs['password'])

        # If failed, try treating it as an email
        if user is None:
            try:
                user_obj = User.objects.get(email=username_or_email)
                user = authenticate(username=user_obj.username, password=password)
            except User.DoesNotExist:
                pass

        if not user:
            raise serializers.ValidationError({
                'non_field_errors': ['Invalid credentials']
            })

        refresh = RefreshToken.for_user(user)
        return {
            'refresh': str(refresh),
            'access': str(refresh.access_token),
            'user': {
                'id': user.id,
                'username': user.username,
                'email': user.email
            }
        }




















# class LogInSerializer(serializers.Serializer):
#     username_or_email = serializers.CharField(required=True)
#     password = serializers.CharField(
#         required=True,
#         write_only=True,
#         style={'input_type': 'password'}
#     )
#
#     def validate(self, attrs):
#
#         user = authenticate(
#             username_or_email=attrs['username_or_email'],
#             password=attrs['password']
#         )
#
#         if not user:
#             raise serializers.ValidationError({
#                 'non_field_errors': ['Invalid credentials']
#             })
#
#         refresh = RefreshToken.for_user(user)
#         return {
#             'refresh': str(refresh),
#             'access': str(refresh.access_token),
#             'user': {
#                 'id': user.id,
#                 'username': user.username,
#                 'email': user.email
#             }
#         }