from django.contrib import admin

# Register your models here.
from django.contrib import admin
from .models import *

class ServiceAdmin(admin.ModelAdmin):
    list_display = ['name']
    search_fields = ['name']

class PhoneInline(admin.TabularInline):
    model = Phone
    extra = 1

class CustomerAdmin(admin.ModelAdmin):
    list_display = ['name', 'address']
    search_fields = ['name', 'address']
    inlines = [PhoneInline]

class ItemInline(admin.TabularInline):
    model = Order_Item
    extra = 1

class OrderAdmin(admin.ModelAdmin):
    def change_done(modeladmin, request, queryset):
        queryset.update(status='4')
    change_done.short_description = "Mark as DONE"

    def pending_services(self, obj):
        return Order_Item.objects.filter(order=obj).filter(done=False).count()
    pending_services.allow_tags = True
    pending_services.short_description = u'Pending Services'

    list_display = ['order_id', 'date', 'customer', 'status', 'pending_services']
    list_display = ['order_id', 'date', 'customer', 'status', 'pending_services']
    search_fields = ['name', 'address', 'customer__name']
    date_hierarchy = 'date'
    inlines = [ItemInline]
    actions = [change_done]
    list_filter = ['status', 'customer']

admin.site.register(Order, OrderAdmin)
admin.site.register(Customer,CustomerAdmin)
admin.site.register(Service, ServiceAdmin)
