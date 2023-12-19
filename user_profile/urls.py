from django.urls import path
from .views import ProfileDetailsView

app_name = 'user_profile'
urlpatterns = [
    path('profile/<str:username>',ProfileDetailsView.as_view(),name='user-profile-view'),
]
