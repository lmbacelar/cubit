from django.contrib import admin

from .models import Make, MakeModel, Item


class MakeModelInline(admin.TabularInline):
    model = MakeModel
    extra = 0


class ItemInline(admin.TabularInline):
    model = Item
    extra = 0


class MakeAdmin(admin.ModelAdmin):
    search_fields = ('name', )
    inlines = [MakeModelInline]


class MakeModelAdmin(admin.ModelAdmin):
    list_display = ('model', 'name', 'make')
    search_fields = ('model', 'name', 'make__name')
    inlines = [ItemInline]


class ItemAdmin(admin.ModelAdmin):
    list_display = ('reference', 'name', 'make_model', 'serial_number')
    list_filter = ('updated_at', )
    search_fields = ('reference', 'serial_number', 'make_model__model', 'make_model__make__name')


admin.site.register(Make, MakeAdmin)
admin.site.register(MakeModel, MakeModelAdmin)
admin.site.register(Item, ItemAdmin)
