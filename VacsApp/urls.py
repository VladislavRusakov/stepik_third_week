from django.urls import path, include

from . import views

urlpatterns = [
    path('', views. , name="vacs_main"),
    path('<int:id>', views. , name="exact_vac"),
    path('<str:fckngcat>/<str:spec>',views. , name="spec"),
]
