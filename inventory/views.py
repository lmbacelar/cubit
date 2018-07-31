from django.http import HttpResponse

from .models import Item


def index(request):
    latest_item_list = Item.objects.order_by('-created_at')[:5]
    output = 'Currently on Inventory: ' + ','.join([i.__str__() for i in latest_item_list])
    return HttpResponse(output)

def detail(request, item_id):
    return HttpResponse("You're looking at Item %s." % item_id)
