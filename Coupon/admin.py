from django.contrib import admin
from .models import Coupon


class CouponAdmin(admin.ModelAdmin):
    list_display = ['code', 'valid_from', 'valid_to', 'discount', 'active']
    list_filter = ['active', 'valid_from', 'valid_to', 'active', 'discount']
    search_fields = ['code']
admin.site.register(Coupon, CouponAdmin)
# Register your models here.
