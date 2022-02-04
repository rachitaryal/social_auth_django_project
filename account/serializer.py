from rest_framework import serializers

from account.models import User


class UserInfoShowSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['username', 'email', 'phone', 'first_name', 'last_name', 'gender', 'is_active', 'bio']
        read_only_fields = fields


class UserRegisterSerializer(serializers.ModelSerializer):
    password = serializers.CharField(min_length=6, max_length=110, write_only=True)

    class Meta:
        model = User
        fields = ['username', 'password', 'email', 'phone', 'first_name', 'last_name', 'gender', 'bio']
