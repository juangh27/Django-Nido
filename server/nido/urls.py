from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('/test', views.nido_index, name='nido_index')
]
