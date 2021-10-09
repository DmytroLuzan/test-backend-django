from django.urls import path
from list_groups import views

urlpatterns = [
    path("", views.ListGroupsAPIView.as_view(), name="list_groups_list"),
    path("create/", views.CreateListGroupsAPIView.as_view(), name="list_groups_create"),
    path("update/<int:pk>/", views.UpdateListGroupsAPIView.as_view(), name="update_list_groups"),
    path("delete/<int:pk>/", views.DeleteListGroupsAPIView.as_view(), name="delete_list_groups"),
]