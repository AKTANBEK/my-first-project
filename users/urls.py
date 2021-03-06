from django.contrib.auth.views import LogoutView, LoginView
from django.urls import path
from .views import register


urlpatterns = [
    path('registration/', register, name='registration'),
    path('login/', LoginView.as_view(template_name='users/login.html'), name='login'),
    path('logout/', LogoutView.as_view(template_name='users/logout.html'), name='logout'),
]