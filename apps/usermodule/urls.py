from django.urls import path
from . import views


urlpatterns = [
    path('student/city/', views.show_city, name="city")
]