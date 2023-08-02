from rest_framework.generics import GenericAPIView
from rest_framework.response import Response
from rest_framework import status
from django.contrib.auth import authenticate
from rest_framework.authtoken.models import Token
from rest_framework.permissions import AllowAny
from .serializers import UsersSerializer


class LoginView(GenericAPIView):
    serializer_class = UsersSerializer  # Assuming you have a UserSerializer
    permission_classes = [AllowAny]

    def post(self, request):
        username = request.data.get('username')
        password = request.data.get('password')
        user = authenticate(username=username, password=password)
        if user and user.is_superuser:
            token, _ = Token.objects.get_or_create(user=user)
            print(token.key)
            return Response({'token': token.key}, status=status.HTTP_200_OK)

        return Response({'detail': 'Invalid credentials or not a superuser'}, status=status.HTTP_400_BAD_REQUEST)
