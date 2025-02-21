from django.contrib import admin
from .models import ServiceRequest

@admin.register(ServiceRequest)
class ServiceRequestAdmin(admin.ModelAdmin):
    list_display = ('id', 'customer', 'request_type', 'status', 'created_at')
    list_filter = ('status', 'request_type')
    search_fields = ('customer__username', 'details')
    readonly_fields = ('created_at',)
    fieldsets = (
        (None, {
            'fields': ('customer', 'request_type', 'details', 'status')
        }),
        ('Dates', {
            'fields': ('created_at', 'resolved_at'),
            'classes': ('collapse',)
        }),
        ('Attachment', {
            'fields': ('attachment',),
            'classes': ('collapse',)
        })
    )
