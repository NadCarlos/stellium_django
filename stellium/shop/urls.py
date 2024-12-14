from django.urls import path

from shop.views.shop import (
    ShopIndex,
)


urlpatterns = [
    path(route='shop/', view=ShopIndex.as_view(), name='shop'),
]