from django.urls import path

from blog.views.blog import (
    BlogIndex,
    CategoryList,
    PostList,
    Post,
)


urlpatterns = [
    path(route='index_blog/', view=BlogIndex.as_view(), name='index_blog'),
    path(route='categories/', view=CategoryList.as_view(), name='categories'),
    path(route='posts/<int:id>/', view=PostList.as_view(), name='posts'),
    path(route='post/<int:id>/', view=Post.as_view(), name='post'),
]