from django.urls import path
from .views import BookListCreate, BookRetrieveUpdateDelete

urlpatterns = [
    # Endpoint for creating a new book and listing all books
    path('api/book', BookListCreate.as_view(), name="Create-Book-List"),

    # Endpoint for retrieving, updating, and deleting a specific book by its ID
    path('api/book/<int:pk>/', BookRetrieveUpdateDelete.as_view(), name="Book-Details")
]
