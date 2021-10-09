from rest_framework import serializers
from list_users.models import ListUsers

class ListUsersSerializer(serializers.ModelSerializer):
    class Meta:
        model = ListUsers
        fields = '__all__'