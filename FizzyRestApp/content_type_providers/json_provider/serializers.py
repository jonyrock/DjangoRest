from django.forms import widgets
from rest_framework import serializers
from FizzyRestApp.models import Task

class TaskSerializer(serializers.Serializer):
    pk = serializers.Field()  # Note: `Field` is an untyped read-only field.
    title = serializers.CharField(max_length=100, min_length=0)
    fileUrl = serializers.URLField(max_length=100)

    def restore_object(self, attrs, instance=None):
        """
        Create or update a new snippet instance, given a dictionary
        of deserialized field values.

        Note that if we don't define thi    `s method, then deserializing
        data will simply return a dictionary of items.
        """
        if instance:
            # Update existing instance
            instance.title = attrs.get('title', instance.title)
            instance.fileUrl = attrs.get('language', instance.fileUrl)
            return instance

        # Create new instance
        return Task(**attrs)