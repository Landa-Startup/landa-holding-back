from django.urls import reverse
from django.core.files.uploadedfile import SimpleUploadedFile

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
        file_content = open(r'/home/pedram/Pictures/Untitled.jpeg', 'rb').read()
        file = SimpleUploadedFile('test_file.jpg', file_content, content_type='image/jpeg')

        data = {
            'firstName': 'test first',
            'lastName': 'test last',
            'email': 'test@example.com',
            'phoneNumber': '09336157525',
            'svFile': file
        }

        response = self.client.post(url, data=data, format='multipart')
        self.assertEquals(response.status_code, status.HTTP_201_CREATED)

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
