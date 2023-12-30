from django.urls import reverse
from rest_framework.test import APITestCase
from rest_framework.status import HTTP_200_OK
from .models import Profile


class ProfileTests(APITestCase):
    def setUp(self):
        Profile.objects.create(
            username='test-testi',
            first_name='test first',
            last_name='test last',
            phone_number='09129994444',
            email='test@example.com',
            job_title='back end',
        )

    def test_get_profile(self):
        url = reverse('user_profile:user-profile-view', kwargs={'username': 'test-testi'})
        response = self.client.get(url, format('json'))
        self.assertEquals(response.status_code, HTTP_200_OK)

    def test_contain_get_profile(self):
        url = reverse('user_profile:user-profile-view', kwargs={'username': 'test-testi'})
        respose = self.client.get(url, format('json'))
        self.assertContains(respose, 'test first')
