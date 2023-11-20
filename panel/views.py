from urllib import response
import uuid
from django.http import HttpResponse,Http404
from django.shortcuts import render
from .serializers import VacationGetAllFormSerializer,VacationSerializers,CreateVacationSerializers
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.generics import CreateAPIView,DestroyAPIView
from rest_framework import status
from rest_framework.permissions import IsAuthenticated
from .models import Vacation
from accounts.permissions import CanViewVacation,CanCreateVacation,CanGetAllVacation,CanEditVacation,CanDeleteVacation

# Create your views here.

########## vacation form apis ##########
class VacationGetAllForm(APIView):
    permission_classes=[CanGetAllVacation,IsAuthenticated]
    def get(self,request):
        queryset = Vacation.objects.all()# Query your model for data
        serializer = VacationGetAllFormSerializer(queryset, many=True)  # Serialize the data
        return Response(serializer.data)
    

class VacationCreateForm(CreateAPIView):
    permission_classes=[CanCreateVacation,IsAuthenticated]
    queryset = Vacation.objects.all()# Query your model for data
    http_method_names = ['post']
    serializer_class = CreateVacationSerializers  # Serialize the data

class VacationEditForm(APIView):
    serializer_class = VacationSerializers
    
    def get_object(self, pk):
        try:
            return Vacation.objects.get(pk=pk, user_id__employer_id=self.request.user.id)
        except Vacation.DoesNotExist:
            raise Http404
    
    def put(self, request, pk, format=None):
        # get object with primary key pk
        obj = self.get_object(pk)  

        # serialize data from request 
        serializer = self.serializer_class(obj, data=request.data, partial=True) 
        
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class VacationDeleteForm(DestroyAPIView):
    permission_classes=[CanDeleteVacation,IsAuthenticated]
    queryset = Vacation.objects.all()# Query your model for data
    serializer = VacationSerializers(queryset, many=True)  # Serialize the data

class VacationViewForm(APIView):
    permission_classes = [CanViewVacation,IsAuthenticated]
    def get(self,request):
        queryset = Vacation.objects.all().filter(user_id=request.user.id)
        serializer = VacationSerializers(queryset, many=True)
        return Response(serializer.data)

class VacationViewStaffForm(APIView):
    permission_classes = [CanViewVacation,CanEditVacation,IsAuthenticated]
    def get(self,request):
        get_all_objects = Vacation.objects.all()
        queryset = get_all_objects.filter(user_id__employer=request.user.id).exclude(user_id=request.user.id)
        serializer = VacationSerializers(queryset, many=True)
        return Response(serializer.data)


def approve(request,uuid_value):
    try:
        # Attempt to convert the URL parameter to a UUID object
        uuid_obj = uuid.UUID(uuid_value)
        # You can now use uuid_obj in your view logic
        vacation_form = Vacation.objects.get(uuid=uuid_obj)
        vacation_form.status = 2
        vacation_form.save()
        print(vacation_form.status)
        return render(request,'panel/vacation_change_status.html',{"status":"Approved"})
    except ValueError:
        # Handle the case where the URL parameter is not a valid UUID
        return render(request,'panel/invalid_vacation.html',{})


def decline(request,uuid_value):
    try:
        # Attempt to convert the URL parameter to a UUID object
        uuid_obj = uuid.UUID(uuid_value)
        # You can now use uuid_obj in your view logic
        vacation_form = Vacation.objects.get(uuid=uuid_obj)
        vacation_form.status = 3
        vacation_form.save()
        print(vacation_form.status)
        return render(request,'panel/vacation_change_status.html',{"status":"Declined"})
    except ValueError:
        # Handle the case where the URL parameter is not a valid UUID
        return render(request,'panel/invalid_vacation.html',{})
