from django.urls import path
from . import views
from django.contrib.auth import views as auth_views
from .views import CreatePost, DeletePost, UpdatePost, ListPosts, PostDetails
urlpatterns = [
    path('', views.home, name='home'),
    path('login/',auth_views.LoginView.as_view(template_name ='registration/login.html'),name = 'login'),
    path('register/', views.register, name ='register'),
    path('logout/',auth_views.LogoutView.as_view(template_name='registration/logout.html'),name = 'logout'),
    path('profile/', views.profile, name='profile'),
    path('/posts/', ListPosts.as_view(), name='posts'),
    path('/post/new/', CreatePost.as_view(), name='new-post'),
    path('/posts/<int:pk>/', PostDetails.as_view(), name= 'post-details'),
    path('/post/<int:pk>/update/', UpdatePost.as_view(), name='update-post'),
    path('/post/<int:pk>/delete/', DeletePost.as_view(), name='delete-post')
]
