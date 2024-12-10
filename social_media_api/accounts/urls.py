from django.urls import path
from . import views
from django.contrib.auth import views as auth_views
urlpatterns = [
    path('login/', auth_views.LoginView(template_name='registration/login.html'),name='login'),
    path('logout/', auth_views.LogoutView(template_name='registration/logout.html'),name='logout'),
    path('register/', views.register, name='register'),
    path('profile/',views.profile, name='profile')

]
