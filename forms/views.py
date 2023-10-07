from django.http import HttpResponse
from .models import Vacation
import uuid
from rest_framework.generics import CreateAPIView
from django.views.generic import DetailView
from rest_framework.views import APIView
from django.middleware.csrf import get_token
from rest_framework.response import Response
from rest_framework.parsers import FormParser,MultiPartParser
from .models import StartUpsForm,ContactUs,PartnerMembership,InvestorRegistration,Entrepreuneur,ApplyJob
from .serializers import StartupFormSerializer,ContactUsSerializer,PartnerMembershipSerializer,InvestorRegistrationSerializer,EntrepreuneurSerializer,ApplyJobSerializer
# Create your views here.

class StartUpsFormView(CreateAPIView):
    queryset = StartUpsForm.objects.all() #TODO: delete this statement
    serializer_class = StartupFormSerializer
    parser_classes = [FormParser,MultiPartParser]
    http_method_names = ['post']

class ContactUsView(CreateAPIView):
    queryset = ContactUs.objects.all()
    serializer_class = ContactUsSerializer
    http_method_names = ['post']

class PartnerMembershipView(CreateAPIView):
    queryset = PartnerMembership.objects.all()
    serializer_class = PartnerMembershipSerializer
    http_method_names = ['post']

class InvestorRegistrationView(CreateAPIView):
    queryset = InvestorRegistration.objects.all()
    serializer_class = InvestorRegistrationSerializer
    http_method_names = ['post']

class EntrepreuneurView(CreateAPIView):
    queryset = Entrepreuneur.objects.all()
    serializer_class = EntrepreuneurSerializer
    http_method_names = ['post']

class ApplyJobView(CreateAPIView):
    queryset = ApplyJob.objects.all()
    serializer_class = ApplyJobSerializer
    http_method_names = ['post']


def approve(requests,uuid_value):

    try:
        # Attempt to convert the URL parameter to a UUID object
        uuid_obj = uuid.UUID(uuid_value)
        # You can now use uuid_obj in your view logic
        vacation_form = Vacation.objects.get(uuid=uuid_obj)
        vacation_form.status = 2
        vacation_form.save()
        print(vacation_form.status)
        return HttpResponse(f'UUID: {uuid_obj}')
    except ValueError:
        # Handle the case where the URL parameter is not a valid UUID
        return HttpResponse('Invalid UUID', status=400)
    




def decline(requests,uuid_value):
    try:
        # Attempt to convert the URL parameter to a UUID object
        uuid_obj = uuid.UUID(uuid_value)
        # You can now use uuid_obj in your view logic
        vacation_form = Vacation.objects.get(uuid=uuid_obj)
        vacation_form.status = 3
        vacation_form.save()
        print(vacation_form.status)
        return HttpResponse(f'UUID: {uuid_obj}')
    except ValueError:
        # Handle the case where the URL parameter is not a valid UUID
        return HttpResponse('Invalid UUID', status=400)


# csrf token 
class CSRFTokenView(APIView):
    def get(self, request, format=None):
        token = get_token(request)
        return Response({'csrfToken': token})