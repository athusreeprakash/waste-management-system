from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),

    path('login/', views.login, name='login'),
    path('logout/', views.logout, name='logout'),

    path('user_register/', views.user_register, name='user_register'),
    path('collector_register/', views.collector_register, name='collector_register'),

    path('request_pickup/', views.request_pickup, name='request_pickup'),
    path('pickup_status/', views.pickup_status, name='pickup_status'),

    path('add_category/', views.add_category, name='add_category'),
    path('add_product/', views.add_product, name='add_product'),

    path('complaints/', views.complaints, name='complaints'),

    path('purchase/', views.purchase, name='purchase'),
    path('order_updates/', views.order_updates, name='order_updates'),
]
