from django.db import models
from to_do_app import settings
# Create your models here.
class UserRegister(models.Model):
    username =models.CharField(max_length=200)
    useremail =models.EmailField()
    userpassword =models.CharField(max_length =200)
    userimage =models.ImageField(upload_to ='user-profiles',default ='/user-profiles/default.png',blank =True)
    usermobilenumber =models.CharField(max_length =200,blank=True)
    userdob =models.DateField(default='2021-12-19')

    def __str__(self):
        return self.username
