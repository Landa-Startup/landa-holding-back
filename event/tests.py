import os
from PIL import Image, ImageDraw

from django.urls import reverse
from django.core.files.uploadedfile import SimpleUploadedFile
from django.conf import settings

from rest_framework.test import APITestCase
from rest_framework import status

from .models import *


class EventForms(APITestCase):
    def setUp(self):
        Event.objects.create(
            slug='test-api',
            start_date='2023-12-23T00:00:00+03:30',
            end_date='2024-01-05T00:00:00+03:30',
            description='some random text',
        )
        Event.objects.create(
            slug='test2-api',
            start_date='2022-12-23T00:00:00+03:30',
            end_date='2023-01-05T00:00:00+03:30',
            description='some random text 2',
        )

    def test_event_list(self):
        url = reverse('event:list')

        response = self.client.get(url, format='json')
        self.assertEquals(response.status_code, status.HTTP_200_OK)
        self.assertEquals(Event.objects.all().count(), 2)
        self.assertContains(response, 'test-api')
        self.assertContains(response, 'test2-api')

    def test_event_details(self):
        url = reverse('event:details', kwargs={'slug': 'test2-api'})

        response = self.client.get(url, format='json')
        self.assertEquals(response.status_code, status.HTTP_200_OK)
        self.assertContains(response, 'test2-api')

    def test_event_register(self):
        url = reverse('event:register')

        data = {
            'event': '1',
            'email': 'test@example.com',
            'phone': '09123456789',
            'reserved_count': '1'
        }
        response = self.client.post(url, data=data, format='json')
        self.assertEquals(response.status_code, status.HTTP_201_CREATED)

    def test_event_image(self):
        url = reverse('event:details', kwargs={'slug': 'test-api'})

        os.chdir(str(settings.BASE_DIR) + '/media/events/images')

        # START: create an example image on the root
        width, height = 300, 200
        image = Image.new("RGB", (width, height), "white")
        draw = ImageDraw.Draw(image)
        draw.rectangle([50, 50, 250, 150], fill="red")
        image.save("event_image.png")
        # file uploader for data
        file_content = open('event_image.png', 'rb').read()
        file = SimpleUploadedFile('test_event_image.jpg', file_content, content_type='image/jpeg')

        os.remove('event_image.png')
        # END: deleted the example image

        instance = Images.objects.create(image=file, event_id=1)
        response = self.client.get(url, format='json')
        self.assertContains(response, instance.image.url)
        # delete the exmple file
        os.remove('test_event_image.jpg')
