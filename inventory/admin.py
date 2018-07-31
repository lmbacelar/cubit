from django.contrib import admin

from .models import Make, MakeModel, Item

admin.site.register(Make)
admin.site.register(MakeModel)
admin.site.register(Item)
