from rest_framework import serializers


class BlogSerializer(serializers.Serializer):

    def create(self, validated_data):
        pass

    def update(self, instance, validated_data):
        pass