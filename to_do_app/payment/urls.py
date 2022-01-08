from django.contrib import admin
from django.urls import path
from stripe.api_resources import payout
from .views import (
    CreateCheckoutSessionView,
    CancelView,
    SuccessView,
    checkoutpage,
    payout_create
)

urlpatterns = [
    path('checkout/',checkoutpage,name ='checkout'),
    path('cancel/', CancelView, name='cancel'),
    path('success/', SuccessView, name='success'),
    path('create-checkout-session/', CreateCheckoutSessionView.as_view(), name='create-checkout-session'),
    path('payout/', payout_create, name='payout'),
]