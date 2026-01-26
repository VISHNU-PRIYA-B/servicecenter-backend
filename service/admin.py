from django.contrib import admin
from .models import Estimation,Invoice

@admin.register(Estimation)
class EstimationAdmin(admin.ModelAdmin):
    list_display = ('repair_request', 'subtotal','tax','total', 'approved')
    list_filter = ('approved',) 
    search_fields = ('repair_request_id',) 

@admin.register(Invoice)
class InvoiceAdmin(admin.ModelAdmin):
    list_display = ('repair_request', 'total_amount', 'parts_replaced', 'notes')