from typing import List, Optional

from shop.models import Product


class ProductRepository:

    def get_all(self) -> List[Product]:
        return Product.objects.all()
    
    def filter_by_id(self, id) -> Optional[Product]:
        return Product.objects.filter(id=id).first()
    
    def filter_by_activo(self) -> List[Product]:
        return Product.objects.filter(
            activo=True
        ).order_by('name')
    
    def delete_by_activo(self, product: Product):
        product.activo=False
        product.save()