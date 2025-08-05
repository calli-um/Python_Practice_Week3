from rest_framework import serializers
from .models import CustomUser, Student
from dj_rest_auth.serializers import UserDetailsSerializer


class UserSerializer(serializers.ModelSerializer):
    class Meta(UserDetailsSerializer.Meta):
        model = CustomUser
        fields = ['id', 'username', 'role']

class StudentSerializer(serializers.ModelSerializer):
    user = UserSerializer()
    class Meta:
        model = Student
        fields = '__all__'