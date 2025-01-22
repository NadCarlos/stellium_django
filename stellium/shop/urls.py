from django.urls import path, include

from shop.views.shop import (
    ShopIndex,
    ProductsList,
    ProductDetail,
    PaymentSuccess,
    PaymentSuccessCustom,
    PaymentSuccessConsult,
    PaymentFailed,
    ConsultIndex,
    ConsultCalendar,
)


urlpatterns = [
    path('paypal/', include("paypal.standard.ipn.urls")),
    path(route='', view=ShopIndex.as_view(), name='shop'),
    path(route='products/', view=ProductsList.as_view(), name='products'),
    path(route='<int:id>/product_detail/', view=ProductDetail.as_view(), name='product_detail'),
    path(route='payment_success/',view=PaymentSuccess.as_view(), name='payment_success'),
    path(route='payment_success_custom/',view=PaymentSuccessCustom.as_view(), name='payment_success_custom'),
    path(route='<str:date>/<str:time>/payment_success_consult/',view=PaymentSuccessConsult.as_view(), name='payment_success_consult'),
    path(route='payment_failed/',view=PaymentFailed.as_view(), name='payment_failed'),
    path(route='consult_index/',view=ConsultIndex.as_view(), name='consult_index'),
    path(route='consult_calendar/',view=ConsultCalendar.as_view(), name='consult_calendar'),
]