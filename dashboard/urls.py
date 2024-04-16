from django.urls import path 
from . import views
# dashboard/urls.py
from .views import engineer_dashboard
from .views import customer_dashboard
from .views import admin_dashboard
urlpatterns = [
    path('', views.dashboard, name='dashboard'),
    path('admin/dashboard/', views.admin_dashboard, name='admin_dashboard'),
    path('engineer/dashboard/', views.engineer_dashboard, name='engineer-dashboard'),
    path('customer/dashboard/', views.customer_dashboard, name='customer_dashboard'),
    
]