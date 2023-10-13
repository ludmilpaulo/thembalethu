# project/urls.py
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/information/', include('information.urls')),
    path('api/services/', include('sevice.urls')),  
]
