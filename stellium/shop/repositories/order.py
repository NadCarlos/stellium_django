from typing import List, Optional

from shop.models import Order


class OrderRepository:

    def get_all(self) -> List[Order]:
        return Order.objects.all()
    
    def filter_by_id(self) -> Optional[Order]:
        return Order.objects.filter(id=id).first()
    
    def filter_by_first(self) -> Optional[Order]:
        return Order.objects.filter().first()
    
    def filter_by_activo(self) -> List[Order]:
        return Order.objects.filter(
            activo=True
        ).order_by('nombre')
    
    def filter_by_invoice_id(self, invoice_id) -> List[Order]:
        return Order.objects.filter(invoice_id=invoice_id).first()
    
    def get_by_id(self, id: int) -> Optional[Order]:
        try:
            order = Order.objects.get(id=id)
        except:
            order = None
        return order
    
    def delete(self, order: Order):
        return order.delete()
    
    def create(
        self,
        product_name: str,
        buyer_email: str,
        amount: str,
        currency: str,
        invoice_id: str,
    ):
        return Order.objects.create(
            product_name=product_name,
            buyer_email=buyer_email,
            amount=amount,
            currency=currency,
            invoice_id=invoice_id,
        )