from django.urls import path
from . import views
from django.contrib.auth import views as auth_views
from .views import PostCreateView,PostDeleteView,PostDetailView,PostListView,PostUpdateView
urlpatterns = [
    path('', views.home, name='home'),
    path('login/',auth_views.LoginView.as_view(template_name ='registration/login.html'),name = 'login'),
    path('register/', views.register, name ='register'),
    path('logout/',auth_views.LogoutView.as_view(template_name='registration/logout.html'),name = 'logout'),
    path('profile/', views.profile, name='profile'),
    path('/posts/',PostListView.as_view(), name='posts'),
    path('/post/new/', PostCreateView.as_view(), name='new-post'),
    path('/posts/<int:pk>/', PostDetailView.as_view(), name= 'post-details'),
    path('/post/<int:pk>/update/', PostUpdateView.as_view(), name='update-post'),
    path('/post/<int:pk>/delete/', PostDeleteView.as_view(), name='delete-post')
]
