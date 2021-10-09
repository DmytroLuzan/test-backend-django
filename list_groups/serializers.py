from rest_framework import serializers
from list_groups.models import ListGroups

class ListGroupsSerializer(serializers.ModelSerializer):
    class Meta:
        model = ListGroups
        fields = '__all__'