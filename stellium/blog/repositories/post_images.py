from typing import List, Optional

from blog.models import (
    PostImages,
)


class PostImagesRepository:

    def get_all(self) -> List[PostImages]:
        return PostImages.objects.all()
    
    def filter_by_id(self, id) -> Optional[PostImages]:
        return PostImages.objects.filter(id=id).first()
    
    def filter_by_post(self, id_post) -> Optional[PostImages]:
        return PostImages.objects.filter(id_post=id_post)