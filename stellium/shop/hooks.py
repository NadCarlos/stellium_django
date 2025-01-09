from paypal.standard.models import ST_PP_COMPLETED
from paypal.standard.ipn.signals import valid_ipn_received
from django.dispatch import receiver
from django.conf import settings
from django.core.mail import send_mail


from shop.repositories.product import ProductRepository
from shop.repositories.order import OrderRepository
from shop.repositories.product_file import ProductFileRepository

from django.core.mail import EmailMessage
from django.conf import settings


orderRepo = OrderRepository()
productRepo = ProductRepository()
fileRepo = ProductFileRepository()


def send_purchase_confirmation(product, buyer_email, amount, currency, file):
    subject = "Confirmación de compra"
    message = (
        f"Gracias por tu compra. Detalles:\n\n"
        f"Producto: {product.name}\n"
        f"Precio: {amount} {currency}\n"
        f"Correo: {buyer_email}"
    )

    email = EmailMessage(
        subject=subject,
        body=message,
        from_email=settings.EMAIL_HOST_USER,
        to=[buyer_email],
    )

    # Adjuntar archivo si existe
    if file:
        email.attach_file(file.upload.path)

    email.send(fail_silently=False)


@receiver(valid_ipn_received)
def paypal_payment_received(sender, **kwargs):
    ipn = sender

    if ipn.payment_status == ST_PP_COMPLETED:
        # Obtener detalles del pago
        product_name = ipn.item_name
        product_id = ipn.custom
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

        product = productRepo.filter_by_id(id=product_id)

        if product.product_type == 'fixed':

            file = fileRepo.filter_by_product_id(id_product=product.id)
            
            send_purchase_confirmation(
                product=product,
                buyer_email=buyer_email,
                amount=amount,
                currency=currency,
                file=file
            )
        
        elif product.product_type == 'custom':
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
        
        elif product.product_type == 'consult':
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
        print("Error")