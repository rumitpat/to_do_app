from django.test import TestCase
from Auth.models import UserRegister
from django.urls import reverse

class TestUserLogoutCase(TestCase):
    def setUp(self):
        self.credentials = {
            'username': 'testuser',
            'userpassword': 'password'
            }
        UserRegister.objects.create(**self.credentials)

    def test_logout(self):
        # send login data
        response = self.client.post(reverse('user-login'),data =self.credentials)
        # should be logged in now
        self.assertRedirects(response, '/home/', status_code=response.status_code, 
        target_status_code=200, fetch_redirect_response=True)    
        self.assertNotEqual(response.status_code, 200)
        
        response = self.client.get("/logout/")
        self.assertRedirects(response, '/', status_code=302, 
        target_status_code=200, fetch_redirect_response=True)

    
