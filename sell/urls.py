from django.urls import path
from django.conf.urls import url
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('items/', views.items, name='items'),
    path('thankyou/', views.thankyou, name='thankyou')
]