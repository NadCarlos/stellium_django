from paypal.standard.models import ST_PP_COMPLETED
from paypal.standard.ipn.signals import valid_ipn_received
from django.dispatch import receiver
from django.conf import settings
from django.core.mail import send_mail

from shop.repositories.order import OrderRepository


orderRepo = OrderRepository()


@receiver(valid_ipn_received)
def paypal_payment_received(sender, **kwargs):
    ipn = sender
    print(ipn.payment_status)

"""    if ipn.payment_status == ST_PP_COMPLETED:
        print("completo")
        # Obtener detalles del pago
        product_name = ipn.item_name
        buyer_email = ipn.payer_email
        amount = ipn.mc_gross
        currency = ipn.mc_currency

        # Guardar la orden en la base de datos
        order = orderRepo.create(
            product_name=product_name,
            buyer_email=buyer_email,
            amount=amount,
            currency=currency,
            invoice_id=ipn.invoice,
        )

        # Enviar correo de confirmación
        send_mail(
            subject="Confirmación de compra",
            message=f"Gracias por tu compra. Detalles:\n\n"
                    f"Producto: {product_name}\n"
                    f"Precio: {amount} {currency}\n"
                    f"Correo: {buyer_email}",
            from_email=settings.EMAIL_HOST_USER,
            recipient_list=[buyer_email],
            fail_silently=False,
        )
    else:
        print("Nope")"""