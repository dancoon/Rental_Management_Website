from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('signin/', views.signin, name='signin'),
    path('signup/', views.signup, name='signup'),
    # path('logout/', views.logout, name='logout'),
    path('application/', views.apply_tenancy, name='apply_tenancy'),
    path('tenant/', views.display_tenant_account, name='display_tenant_account'),
    path('tenant/comment/', views.tenant_comment, name='tenant_comment'),
    path('tenant/info/', views.tenant_info, name='tenant_info'),
    path('tenant/rent/', views.tenant_rent, name='tenant_rent'),
    path('tenant/payment/', views.tenant_payment, name='tenant_payment'),
]