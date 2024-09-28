import os
from PIL import Image, ImageDraw

from django.urls import reverse
from django.core.files.uploadedfile import SimpleUploadedFile
from django.conf import settings

from rest_framework.test import APITestCase
from rest_framework import status

from .models import *


class FormsTest(APITestCase):
    def test_landagene_form(self):
        url = reverse('forms:landagene-form')
        data1 = {
            'full_name': 'full test name',
            'email': '.',
            'phone_number': '09336157525',
            'company_name': 'some company name',
        }
        data3 = {
            'full_name': 'full test name',
            'email': 'some@example.com',
            'phone_number': '09336157525',
            'company_name': 'some company name',
        }
        response1 = self.client.post(url, data=data1, format='json')
        response3 = self.client.post(url, data=data3, format='json')
        self.assertEquals(response1.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertEquals(response3.status_code, status.HTTP_201_CREATED)

    def test_handicraft_form(self):
        url = reverse('forms:handicraft-form')
        data1 = {
            'first_name': 'first test',
            'last_name': 'last test',
            'email': '',
            'organization': 'test organization',
        }
        data2 = {
            'first_name': 'first test',
            'last_name': 'last test',
            'email': 'test.test@example.com',
            'organization': 'test organization',
        }
        response1 = self.client.post(url, data=data1, format='json')
        response2 = self.client.post(url, data=data2, format='json')
        self.assertEquals(response1.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertEquals(response2.status_code, status.HTTP_201_CREATED)

    def test_apply_job_form(self):
        url = reverse('forms:apply-job-form')
        os.chdir(str(settings.BASE_DIR) + '/media/cv-files')

        # create an example image on the root
        width, height = 300, 200
        image = Image.new("RGB", (width, height), "white")
        draw = ImageDraw.Draw(image)
        draw.rectangle([50, 50, 250, 150], fill="red")
        image.save("apply_job.png")

        file_content = open('apply_job.png', 'rb').read()
        file = SimpleUploadedFile('test_apply.jpg', file_content, content_type='image/jpeg')

        os.remove('apply_job.png')

        data = {
            'firstName': 'test first',
            'lastName': 'test last',
            'email': 'test@example.com',
            'phoneNumber': '09336157525',
            'cvFile': file
        }

        response = self.client.post(url, data=data, format='multipart')
        instance = ApplyJob.objects.first()
        self.assertEquals(response.status_code, status.HTTP_201_CREATED)
        self.assertEquals(instance.cvFile.url, '/media/cv-files/test_apply.jpg')
        os.remove('test_apply.jpg')
        self.assertEquals(instance.firstName, 'test first')

    def test_entrepreuneur_form(self):
        url = reverse('forms:entrepreuneur-form')

        data = {
            'email': 'test@example.com',
            'companyName': 'some test company',
            'phone': '09336157525',
            'website': 'www.somesite.com',
            'fieldOfProfessional': 'test developer',
        }

        response = self.client.post(url, data=data, format='json')
        create_instance = Entrepreuneur.objects.first()

        self.assertEquals(response.status_code, status.HTTP_201_CREATED)
        self.assertEquals(Entrepreuneur.objects.count(), 1)
        self.assertEquals(create_instance.email, data['email'])

    def test_investorregistration_form(self):
        url = reverse('forms:investor-registration')

        data = {
            'firstName': 'test first',
            'lastName': 'test last',
            'email': 'email@example.com',
            'birthDate': '2022-02-12',
            'countryOfResidence': 'iran',
            'provinceOfResidence': 'isfahan',
            'companyName': 'company test',
            'interests': 'kjhsdff',
            'preferredAreas': 'back-end',
            'howDidYouKnowUs': 'testi',
        }

        response = self.client.post(url, data=data, format='json')
        instance = InvestorRegistration.objects.first()
        self.assertEquals(response.status_code, status.HTTP_201_CREATED)
        self.assertEquals(instance.firstName, 'test first')

    def test_partnermembership_form(self):
        url = reverse('forms:partner-membership')

        data = {
            'firstName': 'test first',
            'lastName': 'test last',
            'email': 'email@example.com',
            'birthDate': '2022-02-12',
            'countryOfResidence': 'iran',
            'provinceOfResidence': 'isfahan',
            'companyName': 'company test',
            'investmentCeiling': 'something',
            'howDidYouknowUs': 'testi',
        }

        response = self.client.post(url, data, format='json')
        instance = PartnerMembership.objects.first()
        self.assertEquals(response.status_code, status.HTTP_201_CREATED)
        self.assertEquals(instance.firstName, 'test first')

    def test_contactus_form(self):
        url = reverse('forms:contactus-form')

        data = {
            'name': 'test',
            'email': 'email@example.com',
            'number': '09336157525',
            'subjact': 'test objact',
            'message': 'djfklhasdlfjhlksjdfh',
        }

        response = self.client.post(url, data, format='json')
        instance = ContactUs.objects.first()
        self.assertEquals(response.status_code, status.HTTP_201_CREATED)
        self.assertEquals(instance.name, 'test')

    def test_startup_form(self):
        url = reverse('forms:startups-form')

        data = {
            'firstName': 'test first',
            'lastName': 'test last',
            'birthDate': '2022-02-21',
            'email': 'email@example.com',
            'countryOfResidence': 'iran',
            'provinceOfResidence': 'isfahan',
            'type': 'MVP',
            'ideaExplanation': 'something testi',
            'getToKnowUs': 'nomokham',
            'productName': 'nomodonam',
            'siteAddress': 'nadaram',
            'customerProblem': 'ndadram',
            'solution': 'nemdonam',
            'productLevel': 'nadaram',
            'scalable': 'ziad',
            'monetizationOfYourPlan': 'nemidonam yanichi',
            'structureOfYourSales': 'yechizi',
            'cooperatedWithInvestors': 'nomokham',
            'customerCharacteristic': 'nemidaonam chie',
            'currentCustomers': 'ye 2000 nafar',
            'estimatedMarketSize': 'bozorg',
            'totalTamSamSom': 'totali right',
            'startupRevenue': 'khali',
            'monthlyIncome': 'yeki 2 milliard',
            'currentInterestRate': '2 milliard',
            'currentRaisedFunding': '1 milliard',
            'neededCapital': 'canadar'
        }

        response = self.client.post(url, data, format='multipart')
        instance = StartUpsForm.objects.first()
        self.assertEquals(response.status_code, status.HTTP_201_CREATED)
        self.assertEquals(instance.firstName, 'test first')
