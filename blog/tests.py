from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase
from .models import *


class BlogTest(APITestCase):
    def setUp(self):
        BlogPost.objects.create(
            title='test blog',
            description='some random descriptions',
            slug='test-blog',
            author='test author',
        )
        BlogPost.objects.create(
            title='test2 blog',
            description='some random descriptions2',
            slug='test2-blog',
            author='test2 author',
        )

    def test_blog_list(self):
        url = reverse('blog:blog-list')
        response = self.client.get(url)
        self.assertEquals(response.status_code, status.HTTP_200_OK)
        self.assertEquals(BlogPost.objects.count(), 2)
        self.assertContains(response, 'test blog')
        self.assertContains(response, 'test2 blog')

    def test_blog_detail(self):
        url = reverse('blog:blog-details', kwargs={'slug': 'test-blog'})
        response = self.client.get(url)
        self.assertEquals(response.status_code, status.HTTP_200_OK)
        self.assertContains(response, 'test blog')

