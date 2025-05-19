from typing import List, Optional

from blog.models import (
    Post,
)

import random


class PostRepository:

    def get_all(self) -> List[Post]:
        return Post.objects.all()
    
    def filter_by_id(self, id) -> Optional[Post]:
        return Post.objects.filter(id=id).first()
    
    def filter_by_category(self, id_category) -> Optional[Post]:
        return Post.objects.filter(id_category=id_category)

    def delete(self, post: Post):
        return post.delete()
    
    def delete_by_activo(self, post: Post):
        post.activo=False
        post.save()

    def reactivate(self, post: Post):
        post.activo=True
        post.save()

    def get_random(self, cantidad) -> Optional[Post]:
        posts = list(Post.objects.all())
        return random.sample(posts, cantidad)
