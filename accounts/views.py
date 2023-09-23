from django.shortcuts import render

# Create your views here.
from rest_framework import generics,permissions,status,views
from rest_framework.response import Response
from knox.models import AuthToken
from knox.views import LoginView,APIView
from rest_framework.authtoken.serializers import AuthTokenSerializer
from .serializers import RegisterSerializer,UserSerializer
from django.contrib.auth import login
from django.core.cache import cache


class RegisterAPI(generics.GenericAPIView):
    serializer_class=RegisterSerializer
    
    def post(self,request,*args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.save()
        return Response({
            "user": UserSerializer(user,context=self.get_serializer_context()).data,
            "token": AuthToken.objects.create(user)[1]
        })

class LoginAPI(LoginView):
    permission_classes = (permissions.AllowAny,)
    global user_role
    def post(self,request,format=None):
        serializer = AuthTokenSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.validated_data['user']
        login(request,user)

        user_role = cache.get('custom_data')

                
        custom_data={"user_role":user_role}
        
        response_data = super(LoginAPI,self).post(request,format=None)
        response_data.data.update(custom_data)
        
        return Response(response_data.data)

    