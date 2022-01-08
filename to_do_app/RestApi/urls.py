from rest_framework import routers
from .views import *
from django.urls import include, path

# router = routers.DefaultRouter()
# router.register(r'userregister', UserRegisterViewSet)


urlpatterns = [
    path('RestApi/',user_register_api),
    path('abc/',UserRegisterApi.as_view()),
    path('generics/',GenericsApiView.as_view())
]