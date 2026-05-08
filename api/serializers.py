
from rest_framework import serializers
from django.contrib.auth.hashers import make_password
from .models import User, Task

class RegisterSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)

    class Meta:
        model = User
        fields = ['username', 'email', 'password', 'role']

    def create(self, validated_data):
        validated_data['password'] = make_password(
            validated_data['password']
        )
        return super().create(validated_data)

class TaskSerializer(serializers.ModelSerializer):
    class Meta:
        model = Task
        fields = ['id', 'title', 'description',
                 'completed', 'created_at']
        read_only_fields = ['created_by', 'created_at']
