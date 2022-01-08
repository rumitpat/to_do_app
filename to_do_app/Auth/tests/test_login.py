from django.test import TestCase
from Auth.models import UserRegister
from django.urls import reverse


class TestUserLoginCase(TestCase):
    def setUp(self):
        self.credentials = {
            'username': 'testuser',
            'userpassword': 'password'
            }
        UserRegister.objects.create(**self.credentials)

    def test_invalid(self):
        payload = {'username':'testus',
                  'userpassword':'password'}
        response = self.client.post(reverse("user-login"), data=payload)
        self.assertNotEqual(response.status_code, 302)

        payload = {'username':'testuse',
                  'userpassword':'passwor'
        }
        response = self.client.post(reverse("user-login"), data=payload)
        self.assertNotEqual(response.status_code, 302)

    def test_login(self):
        # send login data
        response = self.client.post(reverse('user-login'),data =self.credentials)
        # should be logged in now
        self.assertRedirects(response, '/home/', status_code=response.status_code, 
        target_status_code=200, fetch_redirect_response=True)    
        self.assertNotEqual(response.status_code, 200)   

