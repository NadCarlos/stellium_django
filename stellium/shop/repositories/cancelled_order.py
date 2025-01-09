from typing import List, Optional

from shop.models import CancelledOrders, Product


class CancelledOrdersRepository:

    def get_all(self) -> List[CancelledOrders]:
        return CancelledOrders.objects.all()
    
    def filter_by_id(self) -> Optional[CancelledOrders]:
        return CancelledOrders.objects.filter(id=id).first()
        
    def delete(self, order: CancelledOrders):
        return order.delete()
    
    def create(
        self,
        id_product: Product,
    ):
        return CancelledOrders.objects.create(
            id_product=id_product,
        )