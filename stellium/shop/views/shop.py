from django.conf import settings
from django.views import View
from django.shortcuts import render
from django.urls import reverse

from urllib.parse import urlencode

import uuid

from paypal.standard.forms import PayPalPaymentsForm

from shop.repositories.product import ProductRepository
from shop.repositories.cancelled_order import CancelledOrdersRepository


productRepo = ProductRepository()
cancelledOrderRepo = CancelledOrdersRepository()


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
        params = urlencode({"product_id": product.id})
        
        if product.product_type == "fixed":
            success_url = "payment_success"
        elif product.product_type == "custom":
            success_url = "payment_success_custom"
        elif product.product_type == "consult":
            success_url = "payment_success_consult"

        paypal_dict = dict(
            business = settings.PAYPAL_RECEIVER_EMAIL,
			amount = product.price,
			item_name= product.name,
			no_shipping= '2',
			invoice= str(uuid.uuid4()),
			currency_code= 'USD', # EUR for Euros
			notify_url= 'http://{}{}'.format(host, reverse("paypal-ipn")),
			return_url= 'http://{}{}'.format(host, reverse(success_url)),
            cancel_return = "http://{}{}?{}".format(host, reverse("payment_failed"), params),
            custom = int(product.id),
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
    

class PaymentSuccessCustom(View):

    def get(self, request):
        return render(
            request,
            'payment_success_custom.html',
        )
    

class PaymentSuccessConsult(View):

    def get(self, request):
        return render(
            request,
            'payment_success_consult.html',
        )


class PaymentFailed(View):

    def get(self, request):
        product_id = request.GET.get('product_id')
        product = productRepo.filter_by_id(id=product_id)

        cancelledOrder = cancelledOrderRepo.create(
            id_product=product,
        )

        return render(
            request,
            'payment_failed.html',
        )
