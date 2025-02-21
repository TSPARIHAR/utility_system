from django.shortcuts import render, get_object_or_404, redirect
from django.views.generic import ListView, DetailView, CreateView
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin
from .models import ServiceRequest
from .forms import ServiceRequestForm


class ServiceRequestListView(LoginRequiredMixin, ListView):
    model = ServiceRequest
    template_name = 'service_requests/request_list.html'
    context_object_name = 'requests'
    login_url = '/accounts/login/'

    def get_queryset(self):
        return ServiceRequest.objects.filter(customer=self.request.user)

class ServiceRequestDetailView(LoginRequiredMixin, DetailView):
    model = ServiceRequest
    template_name = 'service_requests/request_detail.html'
    context_object_name = 'request'
    login_url = '/accounts/login/'

    def get_queryset(self):
        return ServiceRequest.objects.filter(customer=self.request.user)

class ServiceRequestCreateView(LoginRequiredMixin, CreateView):
    model = ServiceRequest
    form_class = ServiceRequestForm
    template_name = 'service_requests/request_create.html'
    success_url = reverse_lazy('service_requests:list')
    login_url = '/accounts/login/'

    def form_valid(self, form):
        if not self.request.user.is_authenticated:
            return redirect(self.login_url)
        form.instance.customer = self.request.user
        return super().form_valid(form)
