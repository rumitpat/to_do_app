from django.test import TestCase
from Auth.models import UserRegister
from django.urls import reverse


class TestUserRegistationCase(TestCase):
    def setUp(self):
        self.username = 'testuser'
        self.useremail = 'testuser@email.com'
        self.userpassword ='password'
                                    
    def test_signup_page_url(self):
        response = self.client.get("/register/")
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, template_name='Auth/auth-register.html')

    def test_signup_page_view_name(self):
        response = self.client.get(reverse('user-register'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, template_name='Auth/auth-register.html')    

    def test_signup_form(self):
        response = self.client.post(reverse('user-register'), data={
            'username': self.username,
            'useremail': self.useremail,
            'userpassword': self.userpassword,
        }
        self.assertEqual(response.status_code, 302)
        self.assertRedirects(response, '/', status_code=302, 
        target_status_code=200, fetch_redirect_response=True)
        users = UserRegister.objects.all()
        self.assertEqual(users.count(), 1)

 



                             
