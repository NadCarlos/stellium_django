from django.urls import path

from shared_app.views.index import(
    Index,
    Error,
)


urlpatterns = [
    path(route='',view=Index.as_view(), name='index'),
    path(route='error/',view=Error.as_view(), name='error'),
]