from rest_framework import serializers
from .models import Book
from django.utils import timezone


class BookSerializer(serializers.ModelSerializer):
    """
    Serializer class for the Book model.

    This serializer is responsible for converting Book model instances
    into JSON format and vice versa.
    """

    class Meta:

        model = Book  # Model associated with the serializer
        fields = '__all__'  # Include all fields of the model in the serialized output

    def validate(self, data):
        """
        Custom validation method to ensure that the publication date is not in the future.

        """
        if data.get('publication_date') > timezone.now().date():
            raise serializers.ValidationError(
                "publication date cannot be in the future")  # Raise validation error if publication date is in the future
        return data  # Return validated data if publication date is valid
