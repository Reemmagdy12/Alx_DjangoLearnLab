from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status , viewsets,permissions
from .serializers import RegisterSerializer, LoginSerializer
from rest_framework.decorators import action
from .serializers import UserSerializer
from .models import CustomUser

class RegisterView(APIView):
    def post(self, request):
        serializer = RegisterSerializer(data=request.data)
        if serializer.is_valid():
            user = serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class LoginView(APIView):
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
    
class UserViewSet(viewsets.ModelViewSet):
    queryset = CustomUser.objects.all()
    serializer_class = UserSerializer
    permission_classes = [permissions.IsAuthenticated]

    @action(detail=True,methods=['post'])
    def follow(self,request,pk=None):
        user_to_follow = self.get_object()
        if user_to_follow == request.user:
            return Response({'error':'You can not follow yourself'}, status= status.HTTP_400_BAD_REQUEST)
        request.user.following.add(user_to_follow)
        return Response({'sucess':f'You have successfully followed {user_to_follow.username}'})
    
    @action(detail=True,methods=['post'])
    def unfollow(self,request,pk=None):
        user_to_unfollow = self.get_object()
        request.user.following.remove(user_to_unfollow)
        return Response({'sucess':f'You have successfully followed {user_to_unfollow.username}'})