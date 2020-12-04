from django.contrib import admin
from django.urls import path

from VacsApp import views

handler404 = views.not_found_handler
handler500 = views.internal_server_error_handler
urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.main_view, name='main'),
    path('vacancies/', views.vacancies_list_view, name="vacancies_list"),
    path('vacancies/<int:id>', views.exact_vac_view, name="exact_vac"),
    path('vacancies/<str:spec>', views.spec_view, name="spec"),
    path('companies/<int:id>', views.comp_view, name="comp"),
]
