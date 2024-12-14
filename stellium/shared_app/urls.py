from django.urls import path

from shared_app.views.index import(
    Index,
)


urlpatterns = [
    path(route='',view=Index.as_view(), name='index'),
]