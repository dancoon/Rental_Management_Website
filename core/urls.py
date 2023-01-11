from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('signin/', views.signin, name='signin'),
    path('signup/', views.signup, name='signup'),
    # path('logout/', views.logout, name='logout'),
    path('application/', views.apply_tenancy, name='apply_tenancy'),

    #owner
    path('owner/', views.display_admin_account, name='display_admin_account'),

    path('owner/tenantsinfo/', views.owner_tenants_info, name='owner_tenants_info'),

    path('owner/roomsinfo/', views.owner_rooms_info, name='owner_rooms_info'),

    path('owner/rents/', views.view_tenants_pay, name='view_tenants_pay'),
    path('owner/comments/', views.view_comments, name='view_comments'),

    path('owner/enrolltenantsview/', views.enroll_tenants_view, name='enroll_tenants_view'),
    path('owner/enrolltenants/<int:pk>/', views.enroll_tenants, name='enroll_tenants'),
]