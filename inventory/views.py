from django.http import HttpResponse

def index(request):
    return HttpResponse("Hello world! You're at the Inventory index ...")

def detail(request, item_id):
    return HttpResponse("You're looking at Item %s." % item_id)
