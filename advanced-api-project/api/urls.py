from django.urls import path
from .views import BookListView,BookDeleteView,BookCreateView,BookUpdateView,BookDetailView

urlpatterns = [
    path('books',BookListView.as_view(), name='list_view'),
    path('books/<int:pk>', BookDetailView.as_view(), name='detail_view'),
    path('books/create', BookCreateView.as_view(), name = 'create_view'),
    path('books/update/<int:pk>', BookUpdateView.as_view(), name='update_view'),
    path ('books/delete/<int:pk>', BookDeleteView.as_view(), name='delete_view')
]
