from typing import List, Optional

from shop.models import ProductFile


class ProductFileRepository:

    def get_all(self) -> List[ProductFile]:
        return ProductFile.objects.all()
    
    def filter_by_id(self, id) -> Optional[ProductFile]:
        return ProductFile.objects.filter(id=id).first()
    
    def filter_by_product_id(self, id_product) -> Optional[ProductFile]:
        return ProductFile.objects.filter(id_product=id_product).first()