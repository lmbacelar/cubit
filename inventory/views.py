from django.http import HttpResponse
from django.shortcuts import render

from .models import Item


def index(request):
    latest_item_list = Item.objects.order_by('-created_at')[:5]
    context = { 'latest_item_list': latest_item_list }
    return render(request, 'inventory/index.html', context)


def detail(request, item_id):
    return HttpResponse("You're looking at Item %s." % item_id)
