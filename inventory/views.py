from django.shortcuts import render
from django.views import generic

from .models import Make, MakeModel, Item


def index(request):
    """View function for home page of site."""

    num_makes = Make.objects.all().count()
    num_models = MakeModel.objects.all().count()
    num_items = Item.objects.all().count()
    context = {
        'num_makes': num_makes,
        'num_models': num_models,
        'num_items': num_items,
    }
    return render(request, 'index.html', context=context)


class ItemListView(generic.ListView):
    model = Item


class ItemDetailView(generic.DetailView):
    model = Item
