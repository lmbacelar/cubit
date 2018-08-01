from django.shortcuts import render
from django.views import generic

from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin

from .models import Make, MakeModel, Item


@login_required
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


class ItemListView(LoginRequiredMixin, generic.ListView):
    model = Item
    paginate_by = 10


class ItemDetailView(LoginRequiredMixin, generic.DetailView):
    model = Item
