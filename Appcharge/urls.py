"""
by sumit kumar
written by fb.com/sumit.luv

"""
from django.contrib import admin
from django.urls import path,include
from chargepoint import views
from django.contrib.auth.views import LoginView,LogoutView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home_view, name=''),

    path('adminclick', views.adminclick_view),

    path('adminsignup', views.admin_signup_view),
    path('adminlogin', LoginView.as_view(template_name='chargepoint/adminlogin.html')),
    path('afterlogin', views.afterlogin_view, name='afterlogin'),
    path('logout', LogoutView.as_view(template_name='chargepoint/index.html'), name='logout'),
    path('admin-dashboard', views.admin_dashboard_view, name='admin-dashboard'),

    path('admin-chargepoint', views.admin_chargepoint_view, name='admin-chargepoint'), 
    path('admin-add-chargepoint', views.admin_add_chargepoint_view, name='admin-add-chargepoint'),  
    path('admin-view-chargepoint', views.admin_view_chargepoint_view, name='admin-view-chargepoint'), 
    path('admin-update-chargepoint', views.admin_update_chargepoint_view, name='admin-update-chargepoint'), 
    path('admin-approve-chargepoint', views.admin_approve_chargepoint_view, name='admin-approve-chargepoint'), 
    path('delete-chargepoint/<int:pk>', views.delete_chargepoint_view, name='delete-chargepoint'),  
    path('update-chargepoint/<int:pk>', views.update_chargepoint_view, name='update-chargepoint'),
    
    path('admin-client/', views.admin_client_view, name='admin-client'),
    path('admin-client/admin-add-client', views.admin_add_client_view, name='admin-add-client'),
    path('admin-client/admin-view-client/', views.admin_view_client_view, name='admin-view-client'),
    path('admin-client/admin-approve-client/', views.admin_approve_client_view, name='admin-approve-client'),
    path('admin-client/admin-update-client/', views.admin_update_client_view, name='admin-update-client'),
    path('delete-client/<int:pk>/', views.delete_client_view, name='delete-client'),
    path('update-client/<int:pk>/', views.update_client_view, name='update-client'),
    
    path('admin-user/', views.admin_user_view, name='admin-user'),
    path('admin-user/admin-add-user', views.admin_add_user_view, name='admin-add-user'),
    path('admin-user/admin-view-user/', views.admin_view_user_view, name='admin-view-user'),
    path('admin-user/admin-approve-user/', views.admin_approve_user_view, name='admin-approve-user'),
    path('admin-user/admin-update-user/', views.admin_update_user_view, name='admin-update-user'),
    path('delete-user/<int:pk>/', views.delete_user_view, name='delete-user'),
    path('update-user/<int:pk>/', views.update_user_view, name='update-user'),

    path('api/', include('api.urls')),
    

]
