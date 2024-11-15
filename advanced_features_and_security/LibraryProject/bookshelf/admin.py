from django.contrib import admin
from .models import Book
from .models import CustomUser
from django.contrib.auth.admin import UserAdmin

# Register your models here.
class BookAdmin(admin.ModelAdmin):
    list_display = ("title" , "author" , "publication_year")
    search_fields = ("title" , "author")
    list_filter = ("title" , "author")
admin.site.register(Book, BookAdmin)

class CustomUserAdmin(UserAdmin):
    model = CustomUser
admin.site.register(CustomUser, CustomUserAdmin)

