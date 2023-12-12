from rest_framework.generics import CreateAPIView
from rest_framework.views import APIView
from django.middleware.csrf import get_token
from rest_framework.response import Response
from rest_framework.parsers import FormParser, MultiPartParser
from .models import StartUpsForm, ContactUs, PartnerMembership, InvestorRegistration, Entrepreuneur, ApplyJob, \
    LandaGene, Handicraft
from .serializers import StartupFormSerializer, ContactUsSerializer, PartnerMembershipSerializer, \
    InvestorRegistrationSerializer, EntrepreuneurSerializer, ApplyJobSerializer, LandaGeneSerializer, \
    HandicraftSerializer


# Create your views here.

class StartUpsFormView(CreateAPIView):
    queryset = StartUpsForm.objects.all()  # TODO: delete this statement
    serializer_class = StartupFormSerializer
    parser_classes = [FormParser, MultiPartParser]
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


class HandicraftView(CreateAPIView):
    queryset = Handicraft.objects.all()
    serializer_class = HandicraftSerializer
    http_method_names = ['post']


class LandaGeneView(CreateAPIView):
    queryset = LandaGene.objects.all()
    serializer_class = LandaGeneSerializer
    http_method_names = ['post']


# csrf token
class CSRFTokenView(APIView):
    def get(self, request, format=None):
        token = get_token(request)
        return Response({'csrfToken': token})
