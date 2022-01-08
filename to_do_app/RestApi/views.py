from django.shortcuts import render
from rest_framework import viewsets
from rest_framework import permissions
from .serializeres import *
from  Auth.models import *
from app.models import *
from django.http import HttpResponse, JsonResponse
from rest_framework.parsers import JSONParser
# from django.views.decorators.csrf import csrf_exempt
import json
from rest_framework.decorators import api_view,authentication_classes,permission_classes
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import mixins
from rest_framework import generics
from rest_framework.authentication import SessionAuthentication, BasicAuthentication,TokenAuthentication
from rest_framework.permissions import IsAuthenticated

# Create your views here.


# class UserRegisterViewSet(viewsets.ModelViewSet):
#     queryset = UserRegister.objects.all()
#     serializer_class = UaerRegisterSerializer
#     authentication_classes = [TokenAuthentication]
#     permission_classes = [permissions.IsAuthenticated]

class UserRegisterApi(APIView):
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]

    def get(self,request):
        data =UserRegister.objects.all()
        serializeres= UaerRegisterSerializer(data,many=True)
        return Response(serializeres.data)

    def post(self,request):
        userimage = request.FILES.get("userimage")
        data = json.loads(request.POST.get("data"))
        data["userimage"] = userimage
        serializer = UaerRegisterSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=201)
        return Response(serializer.errors, status=400)


@authentication_classes([TokenAuthentication])
@permission_classes([IsAuthenticated])
@api_view(['GET', 'POST'])
def user_register_api(request):
    if request.method == 'GET':
        data =UserRegister.objects.all()
        serializeres= UaerRegisterSerializer(data,many=True)
        return JsonResponse(serializeres.data, safe=False)

    elif request.method == 'POST':
        # data = JSONParser().parse(request)
        userimage = request.FILES["userimage"]
        data = json.loads(request.POST["data"])
        data["userimage"] = userimage
        serializer = UaerRegisterSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data, status=201)
        return JsonResponse(serializer.errors, status=400)


class GenericsApiView(generics.GenericAPIView,mixins.ListModelMixin,mixins.CreateModelMixin,):
    queryset = UserRegister.objects.all()
    serializer_class = UaerRegisterSerializer

    def get(self,request):
        return self.list(request)

    def post(self,request, *args, **kwargs):
        return self.create(request, *args, **kwargs)    