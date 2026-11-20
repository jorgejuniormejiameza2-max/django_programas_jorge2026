
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),

    # Rutas de perfiles
    path('profiles/', include("myapp.urls")),

    # Rutas de programas
    path('programas/', include("myapp.urls")),
]