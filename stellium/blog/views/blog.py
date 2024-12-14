from django.views import View
from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect

from blog.repositories.category import CategoryRepository
from blog.repositories.post import PostRepository


cateRepo = CategoryRepository()
postRepo = PostRepository()


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
        return render(
            request,
            'blog/post.html',
            dict(
                post = post,
            )
        )