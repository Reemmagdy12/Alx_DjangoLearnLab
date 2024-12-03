from django.urls import path
from . import views
from django.contrib.auth import views as auth_views
from .views import PostCreateView,PostDeleteView,PostDetailView,PostListView,PostUpdateView
from .views import CommentCreateView,CommentDeleteView,CommentUpdateView,CommentListView, CommentDetailView
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
    path('/post/<int:pk>/delete/', PostDeleteView.as_view(), name='delete-post'),
    path('/posts/<int:post_id>/comments/',CommentListView.as_view(),name = 'comments'),
    path('/posts/<int:post_id>/comments/<int:pk>/', CommentDetailView.as_view(), name='comment_detail'),
    path('/posts/<int:post_id>/comments/new/',CommentCreateView.as_view(), name='new-comment'),
    path('/posts/<int:post_id>/comments/<int:pk>/update',CommentUpdateView.as_view(), name='update-comment'),
    path('/posts/<int:post_id>/comments/<int:pk>/delete', CommentDeleteView.as_view(),name='delete-comment')

]
