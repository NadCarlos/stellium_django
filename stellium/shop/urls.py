from django.urls import path, include

from shop.views.shop import (
    ShopIndex,
    ProductsList,
    ProductDetail,
    PaymentSuccess,
    PaymentFailed,
)


urlpatterns = [
    path('paypal', include("paypal.standard.ipn.urls")),
    path(route='shop/', view=ShopIndex.as_view(), name='shop'),
    path(route='products/', view=ProductsList.as_view(), name='products'),
    path(route='<int:id>/product_detail/', view=ProductDetail.as_view(), name='product_detail'),
    path(route='payment_success/',view=PaymentSuccess.as_view(), name='payment_success'),
    path(route='payment_failed/',view=PaymentFailed.as_view(), name='payment_failed'),
]