from django import http
from django.shortcuts import render,redirect
from django.views import View
from django.views.generic import TemplateView
# Create your views here.
import stripe
from django.conf import settings
from rest_framework.views import APIView
from django.urls import reverse
stripe.api_key = settings.STRIPE_SECRET_KEY


class CreateCheckoutSessionView(APIView):
    def post(self,*args,**kargs):
        host =self.request.get_host()
        checkout_session = stripe.checkout.Session.create(
            line_items=[
                {
                    # TODO: replace this with the `price` of the product you want to sell
                    'price_data':{
                        'currency':'inr',
                        'unit_amount':1000,
                        'product_data':{
                            'name':"django_books"
                        },    
                    },
                    'quantity': 1,
                },
            ],
            payment_method_types=[
            'card',
            ],
            mode='payment',
            success_url="http://{}{}".format(host,reverse('success')),
            cancel_url="http://{}{}".format(host,reverse('cancel')),
        )
        return redirect(checkout_session.url, code=303)

def SuccessView(request):
    return render(request,'success.html')

def CancelView(request):
    return render(request,'cancel.html')

def checkoutpage(request):
    return render(request,'checkout.html')    

def payout_create(request):
    payout = stripe.Payout.create(amount=5000,currency='usd',)







