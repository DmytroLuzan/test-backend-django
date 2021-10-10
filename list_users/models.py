from django.db import models
from list_groups.models import ListGroups

# Create your models here.
class ListUsers(models.Model):
    username = models.CharField(max_length = 100)
    created = models.DateField(auto_now_add =True)
    group_id = models.ForeignKey(ListGroups, on_delete= models.RESTRICT)

    def __str___(self):
        return self.username

