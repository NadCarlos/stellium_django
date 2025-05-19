from django.views import View
from django.shortcuts import render

from blog.repositories.category import CategoryRepository
from blog.repositories.post import PostRepository
from blog.repositories.post_images import PostImagesRepository
from shop.repositories.product import ProductRepository


cateRepo = CategoryRepository()
postRepo = PostRepository()
postImgRepo = PostImagesRepository()
productRepo = ProductRepository()


class BlogIndex(View):

    def get(self, request):
        return render(
            request,
            'blog/index.html'
        )
    

class CategoryList(View):

    def get(self, request):
        categories = cateRepo.get_all()
        return render(
            request,
            'blog/categories_list.html',
            dict(
                categories = categories,
            )
        )


class PostList(View):

    def get(self, request, id):
        posts = postRepo.filter_by_category(id_category=id)
        return render(
            request,
            'blog/posts_list.html',
            dict(
                posts = posts,
            )
        )
    

class Post(View):

    def get(self, request, id):
        post = postRepo.filter_by_id(id=id)
        post_images = postImgRepo.filter_by_post(id_post=post.id)
        random_posts = postRepo.get_random(cantidad=3)
        random_products = productRepo.get_random_products(cantidad=2, product_type='consult')
        return render(
            request,
            'blog/post.html',
            dict(
                post = post,
                post_images = post_images,
                random_posts = random_posts,
                random_products = random_products,
            )
        )