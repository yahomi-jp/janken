from janken.models import Opponent
from django.http import response
from django.test import TestCase
from django.contrib.auth import get_user_model

UserModel = get_user_model()
# Create your tests here.

class RenderOpponentsTest(TestCase):
    def setUp(self):
        self.user = UserModel.objects.create(
            username = 'test_user',
            password = 'secret',
        )
        self.client.force_login(self.user)

    def test_render_created_opponents(self):
        data1 = {
            'name': 'test1',
        }
        data2 = {
            'name': 'test2',
        }
        data3 = {
            'name': 'test3',
        }
        self.client.post('new/', data1)
        self.client.post('new/', data2)
        self.client.post('new/', data3)
        opponents_count = Opponent.objects.filter(created_by=0).count
        self.assertSetEqual(3, opponents_count)
