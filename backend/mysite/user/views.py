from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
# Create your views here.
from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import authenticate, login
from django.contrib.auth.forms import AuthenticationForm
from rest_framework import generics, permissions
from rest_framework.response import Response
from knox.models import AuthToken
# def register(request):
#     if request.method == 'POST':
#         form = UserCreationForm(request.POST)
#         if form.is_valid():
#             user = form.save()
#             login(request, user)
#             return redirect('home') # change this to your homepage url name
#     else:
#         form = UserCreationForm()
#     return render(request, 'register.html', {'form': form})
#
#
# def login_view(request):
#     if request.method == 'POST':
#         form = AuthenticationForm(data=request.POST)
#         if form.is_valid():
#             user = form.get_user()
#             login(request, user)
#             return redirect('homepage') # change this to your homepage url name
#     else:
#         form = AuthenticationForm()
#     return render(request, 'login.html', {'form': form})
#

class SuperUserLoginView(generics.GenericAPIView):
    permission_classes = (permissions.AllowAny,)

    def post(self, request, *args, **kwargs):
        username = request.data.get('username')
        password = request.data.get('password')
        user = authenticate(request, username=username, password=password)

        if user is not None and user.is_superuser:
            return Response({
                "token": AuthToken.objects.create(user)[1]
            })
        else:
            return Response({"message": "Invalid credentials"}, status=400)