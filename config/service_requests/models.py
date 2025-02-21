from django.db import models
from django.conf import settings
from django.utils import timezone

class ServiceRequest(models.Model):
    REQUEST_TYPES = [
        ('new_connection', 'New Connection'),
        ('meter_issue', 'Meter Issue'),
        ('billing', 'Billing Inquiry'),
        ('safety', 'Safety Concern'),
        ('other', 'Other'),
    ]

    STATUS_CHOICES = [
        ('submitted', 'Submitted'),
        ('in_progress', 'In Progress'),
        ('resolved', 'Resolved'),
        ('closed', 'Closed'),
    ]

    customer = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    request_type = models.CharField(max_length=50, choices=REQUEST_TYPES)
    details = models.TextField()
    status = models.CharField(max_length=50, choices=STATUS_CHOICES, default='submitted')
    created_at = models.DateTimeField(default=timezone.now)
    resolved_at = models.DateTimeField(null=True, blank=True)
    attachment = models.FileField(upload_to='service_requests/', null=True, blank=True)

    def __str__(self):
        return f"Service Request #{self.id} - {self.get_request_type_display()}"

    class Meta:
        ordering = ['-created_at']
        verbose_name = 'Service Request'
        verbose_name_plural = 'Service Requests'
