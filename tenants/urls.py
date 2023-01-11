from django.urls import path
from . import views

urlpatterns = [
    path('', views.display_tenant_account, name='display_tenant_account'),
    path('comment/', views.tenant_comment, name='tenant_comment'),
    path('info/', views.tenant_info, name='tenant_info'),
    path('rent/', views.tenant_rent, name='tenant_rent'),
    path('payment/', views.tenant_payment, name='tenant_payment'),
]