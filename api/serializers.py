from rest_framework import serializers
from api.models import User


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['email', 'name', 'password']

    def create(self, validated_data):
        user = User(email=validated_data['email'], name=validated_data['name'])
        user.set_password(validated_data['password'])
        user.save()
        return user
