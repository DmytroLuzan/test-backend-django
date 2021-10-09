from rest_framework.generics import ListAPIView
from rest_framework.generics import CreateAPIView
from rest_framework.generics import DestroyAPIView
from rest_framework.generics import UpdateAPIView
from list_users.serializers import ListUsersSerializer
from list_users.models import ListUsers

# Create your views here.
class ListUsersAPIView(ListAPIView):
    """This endpoint list all of the available todos from the database"""
    queryset = ListUsers.objects.all()
    serializer_class = ListUsersSerializer

class CreateListUsersAPIView(CreateAPIView):
    """This endpoint allows for creation of a todo"""
    queryset = ListUsers.objects.all()
    serializer_class = ListUsersSerializer

class UpdateListUsersAPIView(UpdateAPIView):
    """This endpoint allows for updating a specific todo by passing in the id of the todo to update"""
    queryset = ListUsers.objects.all()
    serializer_class = ListUsersSerializer

class DeleteListUsersAPIView(DestroyAPIView):
    """This endpoint allows for deletion of a specific Todo from the database"""
    queryset = ListUsers.objects.all()
    serializer_class = ListUsersSerializer
