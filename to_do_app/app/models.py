from django.db import models
from Auth.models import UserRegister
import datetime
# Create your models here.
class TaskData(models.Model):
    user =models.ForeignKey(UserRegister,on_delete=models.CASCADE)
    task_id =models.IntegerField()
    task_name =models.CharField(max_length=200)
    task_details =models.TextField()
    task_created_date =models.DateField(auto_now_add=True)
    test_created_time =models.TimeField(auto_now_add=True)
    task_end_date =models.DateField()
    task_end_time =models.TimeField()
    task_status =models.CharField(max_length =200,default=False)
    task_due_date_color_data =models.CharField(max_length =200,default ='black')


# class SeesionModel(models.Model):
#     user =models.ForeignKey(UserRegister,on_delete=models.CASCADE)
#     session_key =models.ForeignKey()