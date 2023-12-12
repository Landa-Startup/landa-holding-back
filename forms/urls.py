from django.urls import path
from .views import StartUpsFormView,ContactUsView,PartnerMembershipView,InvestorRegistrationView,CSRFTokenView,EntrepreuneurView,ApplyJobView

app_name = "forms"
urlpatterns = [
    path('startups-form',StartUpsFormView.as_view(),name='startups-form'),
    path('contactUs-form',ContactUsView.as_view(),name='contactus-form'),
    path('partner-membership',PartnerMembershipView.as_view(),name='partner-membership'),
    path('investor-registration',InvestorRegistrationView.as_view(),name='investor-registration'),
    path('entrepreuneur-form',EntrepreuneurView.as_view(),name='entrepreuneur-form'),
    path('apply-job-form',ApplyJobView.as_view(),name='apply-job-form'),
    path('get-csrf-token', CSRFTokenView.as_view(), name='get_csrf_token'),
]