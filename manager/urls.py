from django.urls import path
from . import views

urlpatterns = [
    path('', views.display_admin_account, name='display_admin_account'),

    path('tenantsinfo/', views.owner_tenants_info, name='owner_tenants_info'),

    path('roomsinfo/', views.owner_rooms_info, name='owner_rooms_info'),

    path('rents/', views.view_tenants_pay, name='view_tenants_pay'),
    path('comments/', views.view_comments, name='view_comments'),

    path('enrolltenantsview/', views.enroll_tenants_view, name='enroll_tenants_view'),
    path('enrolltenants/<int:pk>/', views.enroll_tenants, name='enroll_tenants'),
]