from django.shortcuts import render
from .models import Course


def home(request):
    return render(request, 'index.html',)


def course(request):
    courses = Course.object.all()
    return render(request, 'templates/courses/courses.html', {courses: 'courses'})