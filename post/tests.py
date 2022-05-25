from django.urls import reverse

from rest_framework import status
from rest_framework.test import APITestCase
from .models import Post


class PostTests(APITestCase):
    def test_get_all_posts(self):
        url = reverse('posts')
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    # if response.status == status.201
    # return ok
    # else:
    # return assertError
    # assert response.status == status.200

    def test_create_post(self):
        data = {
            'id': 50,
            'title': 'test_title',
            'description': 'test_description'
        }
        url = reverse('create_post')  # api/v1/post_create
        response = self.client.post(url, data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_delete(self):
        Post.objects.create(id=50,
                            title='test_title',
                            description='test_description', )
        url = reverse('delete', kwargs={'pk': 50})
        response = self.client.delete(url)
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)

    def test_update_post(self):
        Post.objects.create(id=50,
                            title='test_title',
                            description='test_description', )
        data = {
            'id': 50,
            'title': 'test_title',
            'description': 'test_description'
        }
        url = reverse('update_post', kwargs={'pk': 50})  # api/v1/post_create
        response = self.client.put(url, data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
