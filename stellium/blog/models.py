from django.db import models


class Category(models.Model):

    name = models.CharField(
        max_length=150,
        null=False,
        blank=False,
        verbose_name="name",
        )
    
    def __str__(self):
        return  self.name


class Post(models.Model):

    title = models.CharField(
        max_length=150,
        null=False,
        blank=False,
        verbose_name="title",
        )
    
    content = models.TextField(
        max_length=10000,
        null=False,
        blank=False,
        verbose_name="content",
    )

    id_category = models.ForeignKey(
        Category,
        blank=True,
        null=True,
        on_delete=models.SET_NULL,
        related_name='category',
    )

    cover = models.ImageField(
        upload_to='blog_covers/',
        null=True,
        blank=True,
        )

    def __str__(self):
        return  self.title
    

class PostImages(models.Model):

    id_post = models.ForeignKey(
        Post,
        blank=True,
        null=True,
        on_delete=models.SET_NULL,
        related_name='post',
    )

    image = models.ImageField(
        upload_to='blog_covers/',
        null=True,
        blank=True,
        )
    
    def __str__(self):
        return self.id_post.title