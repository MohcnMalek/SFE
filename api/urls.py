from django.urls import path
from . import views

urlpatterns = [
    path('chargepoints/', views.get_chargepoints),
    path('chargepoints/boot_notification/', views.boot_notification),
    path('chargepoints/status_notification/', views.status_notification),
    path('clients/', views.get_clients),
    path('users/', views.get_users),
    path('charging-sessions/', views.get_charging_sessions),
]
