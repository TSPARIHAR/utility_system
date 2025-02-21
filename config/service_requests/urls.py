from django.urls import path
from . import views

app_name = 'service_requests'

urlpatterns = [
    path('', views.ServiceRequestListView.as_view(), name='list'),
    path('create/', views.ServiceRequestCreateView.as_view(), name='create'),
    path('<int:pk>/', views.ServiceRequestDetailView.as_view(), name='detail'),
]
