from django.contrib import admin
from .models import InvestorRegistration, Entrepreuneur, StartUpsForm, PartnerMembership, ContactUs, ApplyJob, \
    LandaGene, Handicraft

# Register your models here.
admin.site.register(InvestorRegistration)
admin.site.register(Entrepreuneur)
admin.site.register(StartUpsForm)
admin.site.register(PartnerMembership)
admin.site.register(ContactUs)
admin.site.register(ApplyJob)
admin.site.register(Handicraft)
admin.site.register(LandaGene)
