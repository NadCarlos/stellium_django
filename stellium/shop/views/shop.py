from django.conf import settings
from django.views import View
from django.shortcuts import render, redirect
from django.urls import reverse
from django.core.mail import send_mail

from urllib.parse import urlencode
import uuid
from paypal.standard.forms import PayPalPaymentsForm
from calendar import monthcalendar
from datetime import datetime, timedelta

from shop.forms import EmailForm

from shop.repositories.product import ProductRepository
from shop.repositories.order import OrderRepository
from shop.repositories.cancelled_order import CancelledOrdersRepository


productRepo = ProductRepository()
orderRepo = OrderRepository()
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
        order = orderRepo.filter_by_first()
        form = EmailForm(initial={'email':order.buyer_email})

        return render(
            request,
            'payment_success_custom.html',
            dict(
                form = form
            )
        )
    
    def post(self,request):
        form = EmailForm(request.POST)
        sent = False
        if form.is_valid():
            name = form.cleaned_data['name']
            email = form.cleaned_data['email']
            message = form.cleaned_data['message']

            # Enviar correo
            send_mail(
                subject=f"Mensaje de {name}",
                message=f"Nombre: {name}\nEmail: {email}\n\nMensaje:\n{message}",
                from_email=email,
                recipient_list=[settings.EMAIL_HOST_USER],
            )
            sent = True

            return redirect('payment_success')


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


class ConsultIndex(View):

    def get(self, request):
        return render(
            request,
            'consult_index.html'
        )


class ConsultCalendar(View):

    def get(self, request):
        today = datetime.today()
        year = today.year
        month = today.month
        calendar_weeks = monthcalendar(year, month)

        current_week = None
        for i, week in enumerate(calendar_weeks):
            if today.day in week:
                current_week = i
                break

        if current_week is None or current_week == len(calendar_weeks) - 1:
            next_week = today + timedelta(days=7)
            year, month = next_week.year, next_week.month
            calendar_weeks = monthcalendar(year, month)
            current_week = 0

        selected_weeks = []
        same_month_weeks = []

        for week in calendar_weeks[current_week + 1 : current_week + 5]:
            filtered_week = []
            for day in week:
                if day != 0:
                    day_date = datetime(year, month, day)
                    if day_date.weekday() < 5:
                        filtered_week.append(day)
                    else:
                        filtered_week.append(None)
                else:
                    filtered_week.append(None)
            selected_weeks.append(filtered_week[:5])
            same_month_weeks.append(filtered_week[:5])

        selected_weeks_len = len(selected_weeks)
        next_month_weeks = []
        if selected_weeks_len < 3:
            if month == 12:
                month = 1
            else:
                month = month + 1
            calendar_weeks = monthcalendar(year, month)
            
            
            for week in calendar_weeks:
                if len(selected_weeks) < 3:
                    filtered_week = []
                    none_count = 0
                    for day in week:
                        if day != 0:
                            day_date = datetime(year, month, day)
                            if day_date.weekday() < 5:
                                filtered_week.append(day)
                            else:
                                filtered_week.append(None)
                        else:
                            filtered_week.append(None)

                    for x in filtered_week:
                        if x == None:
                            none_count = none_count + 1
                    if none_count != 7:
                        selected_weeks.append(filtered_week[:5])
                        next_month_weeks.append(filtered_week[:5])
        else:
            next_month_weeks = None

        return render(
            request, 
            'consult_calendar.html',
            dict(
                same_month_weeks = same_month_weeks,
                next_month_weeks = next_month_weeks,
                year = year,
                month = month,
            )
        )

