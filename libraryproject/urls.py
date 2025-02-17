from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('books/', include('apps.bookmodule.urls')),
    path('users/', include('apps.usermodule.urls')),

]
