from django.urls import path
from list_users import views

urlpatterns = [
    path("", views.ListUsersAPIView.as_view(), name="list_users_list"),
    path("create/", views.CreateListUsersAPIView.as_view(), name="list_users_create"),
    path("update/<int:pk>/", views.UpdateListUsersAPIView.as_view(), name="update_list_users"),
    path("delete/<int:pk>/", views.DeleteListUsersAPIView.as_view(), name="delete_list_users"),
]