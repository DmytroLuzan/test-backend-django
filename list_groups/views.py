from rest_framework.generics import ListAPIView
from rest_framework.generics import CreateAPIView
from rest_framework.generics import DestroyAPIView
from rest_framework.generics import UpdateAPIView
from list_groups.serializers import ListGroupsSerializer
from list_groups.models import ListGroups

# Create your views here.
class ListGroupsAPIView(ListAPIView):
    """This endpoint list all of the available todos from the database"""
    queryset = ListGroups.objects.all()
    serializer_class = ListGroupsSerializer

class CreateListGroupsAPIView(CreateAPIView):
    """This endpoint allows for creation of a todo"""
    queryset = ListGroups.objects.all()
    serializer_class = ListGroupsSerializer

class UpdateListGroupsAPIView(UpdateAPIView):
    """This endpoint allows for updating a specific todo by passing in the id of the todo to update"""
    queryset = ListGroups.objects.all()
    serializer_class = ListGroupsSerializer

class DeleteListGroupsAPIView(DestroyAPIView):
    """This endpoint allows for deletion of a specific Todo from the database"""
    queryset = ListGroups.objects.all()
    serializer_class = ListGroupsSerializer