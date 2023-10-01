from django.urls import path
from .views import BlogList,BlogDeatialsView

app_name="blog"

urlpatterns = [
    path('list',BlogList.as_view(),name='blog-list'),
    path('details/<slug:slug>/', BlogDeatialsView.as_view(), name='blog-details'),]
