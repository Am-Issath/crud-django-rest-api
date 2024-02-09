from http.client import NOT_FOUND
from rest_framework import generics, status
from rest_framework.response import Response
from book.models import Book
from book.serializers import BookSerializer


class BookListCreate(generics.ListCreateAPIView):
    """
    API endpoint to list all books and create a new book.

    GET: Retrieve a list of all books.
    POST: Create a new book.
    """

    queryset = Book.objects.all()  # Queryset for all books
    serializer_class = BookSerializer  # Serializer class for book data

    def post(self, request, *args, **kwargs):
        """
        Handle POST request to create a new book.

        :param request: HTTP request object
        :param args: Additional positional arguments
        :param kwargs: Additional keyword arguments
        :return: Response with serialized data of the created book or validation errors
        """
        serializer = self.get_serializer(
            data=request.data)  # Initialize serializer with request data
        serializer.is_valid(raise_exception=True)  # Validate serializer data
        serializer.save()  # Save validated data (create new book)
        # Return response with created book data and status code 201
        return Response(serializer.data, status=status.HTTP_201_CREATED)


class BookRetrieveUpdateDelete(generics.RetrieveUpdateDestroyAPIView):
    """
    API endpoint to retrieve, update, or delete a specific book.

    GET: Retrieve details of a specific book.
    PUT: Update details of a specific book.
    DELETE: Delete a specific book.
    """

    queryset = Book.objects.all()  # Queryset for all books
    serializer_class = BookSerializer  # Serializer class for book data

    def delete(self, request, *args, **kwargs):
        """
        Handle DELETE request to delete a specific book.

        :param request: HTTP request object
        :param args: Additional positional arguments
        :param kwargs: Additional keyword arguments
        :return: Response with status code 204 if book is successfully deleted, or 404 if book is not found
        """
        try:
            instance = self.get_object()  # Retrieve the book object to be deleted
            self.perform_destroy(instance)  # Delete the book
        except NOT_FOUND:  # Handle case where book is not found
            # Return response with status code 404
            return Response(status=status.HTTP_404_NOT_FOUND)
        # Return response with status code 204 upon successful deletion
        return Response(status=status.HTTP_204_NO_CONTENT)

    def perform_destroy(self, instance):
        """
        Perform the deletion of a book instance.

        :param instance: Book instance to be deleted
        """
        instance.delete()  # Delete the book instance

    def put(self, request, *args, **kwargs):
        """
        Handle PUT request to update a specific book.

        :param request: HTTP request object
        :param args: Additional positional arguments
        :param kwargs: Additional keyword arguments
        :return: Response with serialized data of the updated book or validation errors
        """
        instance = self.get_object()  # Retrieve the book object to be updated
        # Initialize serializer with instance and request data
        serializer = self.get_serializer(
            instance, data=request.data, partial=False)
        serializer.is_valid(raise_exception=True)  # Validate serializer data
        self.perform_update(serializer)  # Update the book
        # Return response with updated book data
        return Response(serializer.data)
