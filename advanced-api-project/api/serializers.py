from .models import Author, Book
from rest_framework import serializers 
from datetime import date 
#the bookserializer serializes the bookmodel and validates that the publication year is not in the future
class BookSerializer(serializers.ModelSerializer):
    class Meta:
        model= Book
        fields = ['title','publication_year','author']
    def validate(self, data):
        if data['publication_year'] > date.today():
            raise serializers.ValidationError('The Date of the publishing can not be in the future')
        return data 
#the authorserializer serializes the author model and has a nested field from the bookserializer to list the books of the author
class AuthorSerializer(serializers.ModelSerializer):
    books = BookSerializer(many=True, read_only=True))
    class Meta:
        model = Author
        fields = ['name']
    
        

