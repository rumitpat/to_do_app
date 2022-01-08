from  Auth.models import *
from app.models import *
from rest_framework import serializers
from rest_framework.renderers import  JSONRenderer
from rest_framework.parsers import JSONParser
import base64
# class UaerRegisterSerializer(serializers.HyperlinkedModelSerializer):
#     class Meta:
#         model = UserRegister
#         fields = '__all__'

# class UaerRegisterSerializer(serializers.Serializer):
#     username =serializers.CharField(max_length=200)
#     useremail =serializers.EmailField()
#     userpassword =serializers.CharField(max_length =200)
#     userimage =serializers.ImageField(default ='/user-profiles/default.png')
#     usermobilenumber =serializers.CharField(max_length =200)
#     userdob =serializers.DateField(default='2021-12-19')

#     def create(self,validation_data):
#         return UserRegister.objects.create(validation_data)



class UaerRegisterSerializer(serializers.ModelSerializer):
    # userimage = serializers.ImageField(max_length=None, allow_empty_file=True, use_url=True)
    class Meta:
        model = UserRegister
        fields = ('id', 'username', 'useremail', 'userpassword', 'userimage', 'usermobilenumber', 'userdob',)