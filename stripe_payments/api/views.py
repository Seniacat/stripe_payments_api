from itertools import product
from multiprocessing import context
import re
from requests import session
import stripe
from django.conf import settings
from django.http import JsonResponse
from django.shortcuts import get_object_or_404, redirect, render
from django.views import View
from django.views.generic import TemplateView

from .models import Item

stripe.api_key = settings.STRIPE_SECRET_KEY
stripe.api_version = "2020-08-27; orders_beta=v3;"


class SuccessView(TemplateView):
    template_name = 'success.html'


class CancelView(TemplateView):
    template_name = 'cancel.html'


class ItemDetailsView(TemplateView):
    template_name = 'item_page.html'

    def get_context_data(self, **kwargs):
        item_id = kwargs.get('pk')
        item = Item.objects.get(pk=item_id)
        context = super(ItemDetailsView, self).get_context_data(**kwargs)
        context.update({
            'STRIPE_PUBLIC_KEY': settings.STRIPE_PUBLIC_KEY,
            'item': item
        })
        return context


class CreateSessionCheckoutView(View):

    def get(self, request, *args, **kwargs):
        item_id = self.kwargs.get('pk')
        item = Item.objects.get(id=item_id)
        YOUR_DOMAIN = 'http://127.0.0.1:8000'
        try:
            checkout_session = stripe.checkout.Session.create(
                payment_method_types=['card'],
                line_items=[
                {
                    "price_data": {
                        "currency": "usd",
                        "unit_amount": item.price,
                        "product_data": {
                            "name": item.name
                        },
                    },
                    "quantity": 1,
                },
            ],
            mode='payment',
            success_url=YOUR_DOMAIN + '/success/',
            cancel_url=YOUR_DOMAIN + '/cancel/',
            )
            return JsonResponse({"id": checkout_session.id})
        except Exception as e:
            return JsonResponse({'error': str(e)})


