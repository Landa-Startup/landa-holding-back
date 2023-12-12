from django.shortcuts import render
from rest_framework.generics import ListAPIView,RetrieveAPIView,CreateAPIView
from .models import Event,EventForm
from .serializers import EventListSerializers,EventDetailsSerializers,EventFormSerializers
# Create your views here.

class EventsListView(ListAPIView):
    queryset = Event.objects.all()
    serializer_class = EventListSerializers

class EventDetailsView(RetrieveAPIView):
    queryset = Event.objects.all()
    serializer_class = EventDetailsSerializers
    lookup_field = 'slug'
    

class EventFormCreate(CreateAPIView):
    queryset = EventForm.objects.all()
    serializer_class = EventFormSerializers
    http_method_names = ['post']
    