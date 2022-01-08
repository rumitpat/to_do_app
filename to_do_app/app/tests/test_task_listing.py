from django.test import TestCase
from app.models import TaskData
from Auth.models import UserRegister
from django.urls import reverse

class TestTaskListingCase(TestCase):
    def setUp(self):
        self.task_id = '1'
        self.task_name ='testtask'
        self.task_details ='demo'
        self.task_end_date ='2021-12-2'
        self.task_end_time ='1:2:12'
        
        self.credentials = {
            'username': 'testuser',
            'userpassword': 'password'
            }
        UserRegister.objects.create(**self.credentials)
        
    def test_task_listing(self):
        response = self.client.post(reverse('user-login'),data =self.credentials)
        # should be logged in now
        self.assertRedirects(response, '/home/', status_code=response.status_code, 
        target_status_code=200, fetch_redirect_response=True)    
        self.assertNotEqual(response.status_code, 200)
        
        #task create..
        response = self.client.post(reverse('add_task'), data={
            'task_id': self.task_id,
            'task_name': self.task_name,
            'task_details': self.task_details,
            'task_end_date': self.task_end_date,
            'task_end_time': self.task_end_time,
        })
        self.assertEqual(response.status_code, 302)
        self.assertRedirects(response, '/task-lists/', status_code=302, 
        target_status_code=200, fetch_redirect_response=True)
        data = TaskData.objects.all()
        self.assertEqual(data.count(), 1)

        #task lists
        response = self.client.get("/task-lists/")
        for d in data:
            user =d.user
        self.assertEqual(user.username,self.credentials["username"])
        print(TaskData.objects.filter(user =user))    
        self.assertEqual(data.count(), 1)
        self.assertTemplateUsed(response, template_name='app/task-lists.html') 
        self.assertEqual(response.status_code, 200)

        