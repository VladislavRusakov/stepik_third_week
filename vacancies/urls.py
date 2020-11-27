from django.contrib import admin
from django.urls import path, include

from VacsApp import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('VacsApp.urls')),
    path('vacancies/', include('VacsApp.urls')),
    path('companies/<int:id>', views. , name="comp"),
]
