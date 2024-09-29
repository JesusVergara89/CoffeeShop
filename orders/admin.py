from django.contrib import admin
from .models import Order, OrderProduct


class OrderProductInlineAdmin(admin.TabularInline):
    model = OrderProduct
    extra = 0


class OrderAdmin(admin.ModelAdmin):
    model = Order
    inlines = [OrderProductInlineAdmin]
    list_display = ("user", "is_active", "created_at", "updated_at")
    search_fields = ("user",)


admin.site.register(Order, OrderAdmin)
