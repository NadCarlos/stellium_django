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
    
    image = models.ImageField(
        upload_to='product_covers/',
        null=True,
        blank=True,
        )

    active = models.BooleanField(
        default=1,
        null=False,
        blank=False,
        )

    def __str__(self):
        return  self.name


class Order(models.Model):

    STATUS_CHOICES = [
        ('PENDING', 'Pending'),
        ('COMPLETED', 'Completed'),
        ('FAILED', 'Failed'),
    ]

    product_name = models.CharField(
        max_length=255
        )
    
    buyer_email = models.EmailField(
        )

    amount = models.DecimalField(
        max_digits=10,
        decimal_places=2
        )
    
    currency = models.CharField(
        max_length=10, 
        default='EUR'
        )
    
    invoice_id = models.CharField(
        max_length=100,
        unique=True
        )
    
    status = models.CharField(
        max_length=10,
        choices=STATUS_CHOICES,
        default='COMPLETED'
        )
    
    created_at = models.DateTimeField(
        auto_now_add=True
        )
    
    updated_at = models.DateTimeField(
        auto_now=True
        )

    def __str__(self):
        return f"Order {self.invoice_id} - {self.product_name} ({self.status})"
    

class CancelledOrders(models.Model):

    id_product = models.ForeignKey(
        Product,
        blank=False,
        null=True,
        on_delete=models.SET_NULL,
        related_name='product',
    )

    created_at = models.DateTimeField(
        auto_now_add=True
        )
    
    updated_at = models.DateTimeField(
        auto_now=True
        )
    
    def __str__(self):
        return f"Order {self.id_product.name} cancelled"