from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('', views.listar_pub, name='listar_pub'),
    path('pub/<int:pk>/', views.detalle_pub, name='detalle_pub'),
    path('pub/nueva', views.nueva_pub, name='nueva_pub'),
    path('pub/<int:pk>/editar/', views.editar_pub, name='editar_pub'),
]
