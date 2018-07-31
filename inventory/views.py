from django.shortcuts import render, get_object_or_404

from .models import Item


def index(request):
    latest_item_list = Item.objects.order_by('-created_at')[:5]
    context = { 'latest_item_list': latest_item_list }
    return render(request, 'inventory/index.html', context)


def detail(request, item_id):
    item = get_object_or_404(Item, pk=item_id)
    return render(request, 'inventory/detail.html', {'item': item})
