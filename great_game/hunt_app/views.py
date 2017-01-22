from django.shortcuts import render

# Create your views here.

from django.http import HttpResponse
from hunt_app.models import Team,Task
from django.template import RequestContext
from django.shortcuts import render_to_response
from django.http import HttpResponseRedirect, HttpResponse
from django.shortcuts import get_object_or_404, render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from hunt_app.models import Team, Task
from hunt_app.serializers import TeamSerializer, TaskSerializer

class TaskList(APIView):

	def get(self, request):
		tasks = Task.objects.all()
		task_serializer = TaskSerializer(tasks, many = True)
		return Response(task_serializer)

class TeamList(APIView):

	def get(self, request):
		teams = Team.objects.all()
		team_serializer = TeamSerializer(teams, many = True)
		return Response(team_serializer)

def index(request):
    return render(request,'index.html')   

def CountdownTimer(request):
	return render(request, 'CountdownTimer.html')

def panel(request):    
    full=Team.objects.all()        
    return render(request, 'panels.html',
              {'full':full})



