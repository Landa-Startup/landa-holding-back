from django.urls import path
from .views import EventDetailsView,EventsListView,EventFormCreate
app_name = 'event'
urlpatterns = [
    path('list/',EventsListView.as_view(),name="list"),
    path('details/<slug:slug>/',EventDetailsView.as_view(),name="details"),
    path('register/',EventFormCreate.as_view(),name="register"),
]