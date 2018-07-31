from django.views import generic

from .models import Item


class IndexView(generic.ListView):
    template_name = 'inventory/index.html'
    context_object_name = 'latest_item_list'

    def get_queryset(self):
        return Item.objects.order_by('-created_at')[:5]


class DetailView(generic.DetailView):
    model = Item
    template_name = 'inventory/detail.html'
