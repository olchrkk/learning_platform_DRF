from rest_framework.test import APITestCase
from django.urls import reverse
from rest_framework import status

from .constants import USER_DATA, create_user


class CreateUserTest(APITestCase):
    def test_create_user(self):
        url = reverse('customuser-list')
        response = self.client.post(path=url, data=USER_DATA, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)


class ReadeUserTest(APITestCase):

    def setUp(self):
        self.user = create_user()

    def test_read_user_list(self):
        url = reverse('customuser-list')
        response = self.client.get(path=url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_read_user_detail(self):
        url = reverse('customuser-detail', args=[self.user.id])
        response = self.client.get(path=url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)


"""
1) для юзера на обновление и на удаление
2) для модели группы напишеи тоже на создание и тд(тесты не простые)
3) для тестов обновления смотреть поле дэт апдейт(нужно что бы оно менялось)
"""