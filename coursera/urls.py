from django.urls import path
from .views import home, Course


urlpatterns = [
    path('', home),
    path('courses/', Course, name='courses')
]
