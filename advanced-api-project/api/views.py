from django.shortcuts import render
from rest_framework import generics,serializers
from rest_framework.permissions import IsAuthenticatedOrReadOnly, IsAuthenticated
from .models import Book 
from .serializers import BookSerializer

# Create your views here.
#Lists all the instances of the Book model.
class BookListView(generics.ListAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]
#Displays the details of the instance of the Book model.
class BookDetailView(generics.RetrieveAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]
#Creates a new instance of the Book model.
class BookCreateView(generics.CreateAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes =[IsAuthenticated]
    #This function makes sure that the book does not already exist before creating it.
    def create(self, serializer):
        serializer= BookSerializer
        if Book.objects.filter(title =serializer.validated_data['title']).exists():
            raise serializers.ValidationError('A Book with this title already exists')
        serializer.save()
#Updates an existing instance of the Book model.       
class BookUpdateView(generics.UpdateAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes =[IsAuthenticated]
    #This function makes sure thet the instance exists before updating it.
    def update(self, serializer):
        serializer= BookSerializer
        if not Book.objects.filter(title =serializer.validated_data['title']):
            raise serializers.ValidationError('this Book does not exist')
        serializer.save()
#Deletes an instance of the Book model.
class BookDeleteView(generics.DestroyAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes =[IsAuthenticated]





