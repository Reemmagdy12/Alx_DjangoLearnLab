from rest_framework.generics import GenericAPIView
from rest_framework.response import Response
from rest_framework import status , viewsets,permissions
from .serializers import RegisterSerializer, LoginSerializer
from rest_framework.decorators import action
from .serializers import UserSerializer
from .models import CustomUser

class RegisterView(GenericAPIView):
    def post(self, request):
        serializer = RegisterSerializer(data=request.data)
        if serializer.is_valid():
            user = serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class LoginView(GenericAPIView):
    def post(self, request):
        serializer = LoginSerializer(data=request.data)
        if serializer.is_valid():
            return Response({'token': serializer.get_token(None)}, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
    
@login_required
def profile(request):
    if request.method == 'POST' :
        user = request.user
        user.email = request.POST.get('email', user.email)
        user.save()
        redirect('profile')
    else:
        return render (request,'profile.html',{'user':request.user})
    
from rest_framework.generics import GenericAPIView
from rest_framework.response import Response
from rest_framework import status, permissions
from .models import CustomUser

class FollowUserView(GenericAPIView):
    permission_classes = [permissions.IsAuthenticated]

    def post(self, request, user_id):
        try:
            user_to_follow = CustomUser.objects.get(id=user_id)
            if user_to_follow == request.user:
                return Response({'error': "You cannot follow yourself."}, status=status.HTTP_400_BAD_REQUEST)

            request.user.following.add(user_to_follow)
            return Response({'success': f'You are now following {user_to_follow.username}.'})
        except CustomUser.DoesNotExist:
            return Response({'error': "User not found."}, status=status.HTTP_404_NOT_FOUND)

class UnfollowUserView(GenericAPIView):
    permission_classes = [permissions.IsAuthenticated]

    def post(self, request, user_id):
        try:
            user_to_unfollow = CustomUser.objects.get(id=user_id)
            if user_to_unfollow == request.user:
                return Response({'error': "You cannot unfollow yourself."}, status=status.HTTP_400_BAD_REQUEST)

            request.user.following.remove(user_to_unfollow)
            return Response({'success': f'You have unfollowed {user_to_unfollow.username}.'})
        except CustomUser.DoesNotExist:
            return Response({'error': "User not found."}, status=status.HTTP_404_NOT_FOUND)