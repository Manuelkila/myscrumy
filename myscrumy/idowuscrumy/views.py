from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth.models import User
from .models import ScrumyGoals, GoalStatus
from random import randint

# Create your views here.
def index(request):
    return HttpResponse(ScrumyGoals.objects.filter(goal_name='Learn Django'))

def move_goal(request, goal_id):
    goal = ScrumyGoals.objects.get(goal_id =goal_id)
    return HttpResponse(goal.goal_name)

def add_goal(request):
    ScrumyGoals.objects.create(
        user=User.objects.get(username='louis'),
        goal_name='Keep Learning Django',
        goal_id= randint(1000,9999),
        created_by = 'Louis',
        moved_by='Louis',
        owner='Louis',
        goal_status=GoalStatus.objects.get(status_name='Weekly Goal')
    )

def home(request):
    scrumygoal = ScrumyGoals.objects.filter(goal_name='Keep Learning Django')
    output = ', '.join([eachgoal.goal_name for eachgoal in scrumygoal])
    return HttpResponse(output)

