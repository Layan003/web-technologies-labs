from django.shortcuts import render
from django.db.models import Count
from .models import Student, Address

# Create your views here.
def show_city(request):
    students_per_city = Address.objects.annotate(student_count=Count('student'))

    return render(request, 'usermodule/show_city.html', {'students_per_city': students_per_city})