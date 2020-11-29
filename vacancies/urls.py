from django.contrib import admin
from django.urls import path

from VacsApp.views import *

handler404 = not_found_handler
handler500 = internal_server_error_handler
urlpatterns = [
    path('admin/', admin.site.urls),
    path('', main_view, name='main'),
    path('vacancies/', vacancies_list_view, name="vacancies_list"),
    path('vacancies/<int:id>', exact_vac_view, name="exact_vac"),
    path('vacancies/<str:category>/<str:spec>', spec_view, name="spec"),
    path('companies/<int:id>', comp_view, name="comp"),
]
