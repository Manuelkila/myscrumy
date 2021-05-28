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
    all_users = User.objects.all()
    weekly_goals = GoalStatus.objects.get(status_name="Weekly Goal")
    goals_weekly = weekly_goals.scrumygoals_set.all()

    daily_goals = GoalStatus.objects.get(status_name="Daily Goal")
    goals_daily = daily_goals.scrumygoals_set.all()

    verify_goals = GoalStatus.objects.get(status_name="Verify Goal")
    goals_verify = verify_goals.scrumygoals_set.all()

    done_goals = GoalStatus.objects.get(status_name="Done Goal")
    goals_done = done_goals.scrumygoals_set.all()

    
    dictionary = {'users': all_users, 'weekly': goals_weekly, 'daily': goals_daily, 'verify': goals_verify, 'done': goals_done}
    return render(request, "idowuscrumy/home.html", dictionary)

