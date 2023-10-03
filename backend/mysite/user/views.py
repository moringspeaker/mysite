# from rest_framework.generics import GenericAPIView
# from rest_framework.response import Response
# from rest_framework import status
# from django.contrib.auth import authenticate
# from rest_framework.authtoken.models import Token
# from rest_framework.permissions import AllowAny
# from .serializers import UsersSerializer
#
#
# class LoginView(GenericAPIView):
#     serializer_class = UsersSerializer  # Assuming you have a UserSerializer
#     permission_classes = [AllowAny]
#
#     def post(self, request):
#         username = request.data.get('username')
#         password = request.data.get('password')
#         user = authenticate(username=username, password=password)
#         if user and user.is_superuser:
#             token, _ = Token.objects.get_or_create(user=user)
#             print(token.key)
#             return Response({'token': token.key}, status=status.HTTP_200_OK)
#
#         return Response({'detail': 'Invalid credentials or not a superuser'}, status=status.HTTP_400_BAD_REQUEST)

from rest_framework import mixins, generics,viewsets,status
from rest_framework.response import Response
from .serializers import UserRegSerializer,UserLoginSerializer,UserSerializer
from django.contrib.auth import get_user_model
from rest_framework.authtoken.models import Token

User = get_user_model()
class UserRegViewSet(mixins.CreateModelMixin,  mixins.ListModelMixin,viewsets.GenericViewSet):
    """
    create:
        Create a new user instance.
    """
    serializer_class = UserRegSerializer
    queryset = User.objects.all()

    def create(self, request, *args, **kwargs):
        print(request.data)

        existing_user = User.objects.filter(username=request.data.get('username')).first()
        if existing_user:
            return Response({'detail': 'user has existed'}, status=status.HTTP_400_BAD_REQUEST)

        response = super().create(request, *args, **kwargs)

        if response.status_code == status.HTTP_201_CREATED:
            response.data = {'message': 'success'}

        print(response.data)
        print(response.status_code)
        return response

class UserLoginViewSet(mixins.CreateModelMixin, viewsets.GenericViewSet):
    serializer_class = UserLoginSerializer

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.validated_data
        token, created = Token.objects.get_or_create(user=user) #add a user token
        return Response({"user_id": user.id,"username":user.username,"token": token.key}, status=status.HTTP_200_OK)

class UserLogoutViewSet(viewsets.ViewSet):
    def create(self, request):
        request.user.auth_token.delete()    # DRF framework will automatically delete the token when user logout, the token is provided with user.auth_token
        return Response(status=status.HTTP_204_NO_CONTENT)

class UserViewSet(mixins.ListModelMixin,
                  mixins.RetrieveModelMixin,
                  mixins.UpdateModelMixin,
                  mixins.DestroyModelMixin,
                  viewsets.GenericViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer