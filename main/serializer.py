from rest_framework import serializers
from .models import MyUsers, Albums


class UserSerializer(serializers.Serializer):
    email = serializers.EmailField()
    first_name = serializers.CharField(max_length=30)
    last_name = serializers.CharField(max_length=30)
    is_active = serializers.BooleanField()

    def create(self, validated_data):
        return MyUsers.objects.create(**validated_data)

    def update(self, instance, validated_data):
        instance.email = validated_data.get('email', instance.email)
        instance.first_name = validated_data.get('first_name', instance.first_name)
        instance.last_name = validated_data.get('last_name', instance.last_name)
        instance.is_active = validated_data.get('is_active', instance.is_active)

        instance.save()
        return instance


class AlbumSerializer(serializers.HyperlinkedModelSerializer):
    name = serializers.CharField(max_length=40)
    user_id = serializers.CharField(source='MyUsers.email')
    metadata = serializers.JSONField()

    class Meta:
        model = Albums
        fields = ('name', 'user_id', 'metadata',)

    def create(self, validated_data):
        return Albums.objects.create(**validated_data)
