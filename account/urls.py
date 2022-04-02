from django.urls import path
from . import views


urlpatterns = [
    path('account', views.acc, name='account'),
    path('login', views.log, name='login'),
]
