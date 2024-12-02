from django.urls import path
from . import views
from django.contrib.auth import views as auth_views
urlpatterns = [
    path('', views.home, name='home'),
    path('login/',auth_views.LoginView.as_view(template_name ='registration/login.html'),name = 'login'),
    path('register/', views.register, name ='register'),
    path('logout/',auth_views.LogoutView.as_view(template_name='registration/logout.html'),name = 'logout'),
    path('profile/', views.profile, name='profile')
]
