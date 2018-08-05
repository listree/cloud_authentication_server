from django.urls import path

from . import views

urlpatterns = [
    path('chkkey', views.chkkey, name='chkkey'),
    path('genkey', views.genkey, name='genkey')
]