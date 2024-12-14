from django.views import View
from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect


class ShopIndex(View):

    def get(self, request):
        return render(
            request,
            'shop_index.html'
        )