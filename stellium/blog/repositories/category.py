from typing import List, Optional

from blog.models import (
    Category,
)


class CategoryRepository:

    def get_all(self) -> List[Category]:
        return Category.objects.all()
    
    def filter_by_id(self) -> Optional[Category]:
        return Category.objects.filter(id=id).first()

    def delete(self, category: Category):
        return category.delete()
    
    def delete_by_activo(self, category: Category):
        category.activo=False
        category.save()

    def reactivate(self, category: Category):
        category.activo=True
        category.save()