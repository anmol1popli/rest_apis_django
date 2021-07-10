from rest_framework import serializers

from .models import Todo


class TodoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Todo
        fields = ['text', 'id']

    def create(self, validated_data):
        """
        Method to create new instances in Todo model.
        :param validated_data:
        :return:
        """

        return Todo.objects.create(text=validated_data.get('text'))

    def update(self, instance, validated_data):
        """
        Method to update instances of Todo model.
        :param instance:
        :param validated_data:
        :return:
        """

        instance.text = validated_data.get('text', instance.text)
        instance.save()
        return instance
