from django.db import models
from django.contrib.auth.models import User
from django.db.models.deletion import PROTECT

# Create your models here.
class GoalStatus(models.Model):
    status_name = models.CharField(max_length=50)



class ScrumyGoals(models.Model):
    goal_name = models.CharField(max_length=50)
    goal_id = models.IntegerField()
    created_by = models.CharField(max_length=50)
    moved_by = models.CharField(max_length=50)
    owner = models.CharField(max_length=50)
    goal_status = models.ForeignKey(GoalStatus, on_delete=PROTECT)
    user = models.ForeignKey(User, related_name="user_goal", on_delete=models.PROTECT)

   

class ScrumyHistory(models.Model):
    moved_by = models.CharField(max_length=50)
    created_by = models.CharField(max_length=50)
    moved_from = models.CharField(max_length=50)
    moved_to = models.CharField(max_length=50)
    time_of_action = models.DateField()
    goal = models.ForeignKey(ScrumyGoals, on_delete=models.CASCADE)

