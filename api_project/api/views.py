from django.shortcuts import render
from .models import Book 
from .serializers import BookSerializer
from rest_framework import generics 
from rest_framework import viewsets

# Create your views here.
class BookList(generics.ListAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer

class BookViewSet(viewsets.ModelViewSet):
    queryset = Book.objects.all()
    serializer_class = BookSerializer

from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.permissions import IsAdminUser, IsAuthenticated
from rest_framework.authtoken.models import Token
from rest_framework.response import Response
from rest_framework import status


class CustomObtainAuthToken(ObtainAuthToken):
    # Use IsAdminUser or any custom permission
    permission_classes = [IsAdminUser , IsAuthenticated]

    def post(self, request, *args, **kwargs):
        response = super().post(request, *args, **kwargs)
        token, created = Token.objects.get_or_create(user=request.user)
        return Response({'token': token.key}, status=status.HTTP_200_OK)
