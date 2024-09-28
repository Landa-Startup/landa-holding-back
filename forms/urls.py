from django.urls import path
from .views import StartUpsFormView, ContactUsView, PartnerMembershipView, InvestorRegistrationView, CSRFTokenView, \
    EntrepreuneurView, ApplyJobView, HandicraftView, LandaGeneView, WorkWithUsView

app_name = "forms"
urlpatterns = [
    path('startups-form', StartUpsFormView.as_view(), name='startups-form'),
    path('contactUs-form', ContactUsView.as_view(), name='contactus-form'),
    path('partner-membership', PartnerMembershipView.as_view(), name='partner-membership'),
    path('investor-registration', InvestorRegistrationView.as_view(), name='investor-registration'),
    path('entrepreuneur-form', EntrepreuneurView.as_view(), name='entrepreuneur-form'),
    path('apply-job-form', ApplyJobView.as_view(), name='apply-job-form'),
    path('handicraft-form', HandicraftView.as_view(), name='handicraft-form'),
    path('landagene-form', LandaGeneView.as_view(), name='landagene-form'),
    path('work-with-us', WorkWithUsView.as_view(), name='work-with-us'),
    path('get-csrf-token', CSRFTokenView.as_view(), name='get_csrf_token'),
]
