from django.db import models


class Product(models.Model):

    name = models.CharField(
        max_length=150,
        null=False,
        blank=False,
        verbose_name="Name",
        )

    price = models.CharField(
        max_length=50,
        null=False,
        blank=False,
        editable=True,
        verbose_name="Price"
        )

    description = models.CharField(
        max_length=200,
        null=True,
        blank=True,
        verbose_name="Description",
        )

    active = models.BooleanField(
        default=1,
        null=False,
        blank=False,
        )

    def __str__(self):
        return  self.name