from django.conf import settings
from django.views import View
from django.shortcuts import render
from django.urls import reverse

import uuid

from paypal.standard.forms import PayPalPaymentsForm

from shop.repositories.product import ProductRepository


productRepo = ProductRepository()


class ShopIndex(View):

    def get(self, request):
        return render(
            request,
            'shop_index.html'
        )
    

class ProductsList(View):

    def get(self, request):
        products = productRepo.get_all()
        return render(
            request,
            'products.html',
            dict(
                products=products
            )
        )
    

class ProductDetail(View):

    def get(self, request, id):
        product = productRepo.filter_by_id(id=id)
        host = request.get_host()
        paypal_dict = dict(
            business = settings.PAYPAL_RECEIVER_EMAIL,
			amount = product.price,
			item_name= product.name,
			no_shipping= '2',
			invoice= str(uuid.uuid4()),
			currency_code= 'EUR', # EUR for Euros
			notify_url= 'http://{}{}'.format(host, reverse("paypal-ipn")),
			return_url= 'http://{}{}'.format(host, reverse("payment_success")),
			cancel_return= 'http://{}{}'.format(host, reverse("payment_failed")),
        )

        # Create acutal paypal button
        paypal_form = PayPalPaymentsForm(initial=paypal_dict)

        return render(
            request,
            'detail.html',
            dict(
                product=product,
                paypal_form=paypal_form,
            )
        )
    

class PaymentSuccess(View):

    def get(self, request):
        return render(
            request,
            'payment_success.html',
        )


class PaymentFailed(View):

    def get(self, request):
        return render(
            request,
            'payment_failed.html',
        )
