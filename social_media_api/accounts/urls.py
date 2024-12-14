
from django.urls import path, include
from .views import RegisterView, LoginView, UserViewSet
from . import views
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register(r'users', UserViewSet)

urlpatterns = [
    path('register/', RegisterView.as_view(), name='register'),
    path('login/', LoginView.as_view(), name='login'),
    path('profile/',views.profile, name='profile'),
    path('', include(router.urls)),

]