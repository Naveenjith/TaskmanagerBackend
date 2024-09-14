from rest_framework import serializers
from .models import Task
from django.contrib.auth.models import User

class Taskserializer(serializers.ModelSerializer):
    class Meta:
        model=Task
        fields= ['id', 'title', 'description', 'status', 'created_at', 'updated_at']

    def validate(self, data):
        if not data.get('title'):
            raise serializers.ValidationError("The title field cannot be empty.")
        return data

class Userserializer(serializers.ModelSerializer):
    username=serializers.CharField()
    password=serializers.CharField(write_only=True)
    class Meta:
        model=User
        fields=['username','password']

    def create(self,validated_data):
            user=User.objects.create_user(
                username=validated_data['username'],
                password=validated_data['password']
            )
            user.is_active=True
            user.save()
            return user