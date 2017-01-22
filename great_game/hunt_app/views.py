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
from django.http import Http404
from django.core import serializers

class TaskList(APIView):

	def get(self, request):
		tasks = Task.objects.all()
		task_serializer = TaskSerializer(tasks, many = True)
		return Response(task_serializer.data)


	#def post(self, request):
    #    serializer = TaskSerializer(data=request.data)
    #    if serializer.is_valid():
    #        serializer.save()
    #        return Response(serializer.data, status=status.HTTP_201_CREATED)
    #    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)	

 



class TeamList(APIView):

	def get_object(self, pk):
		try:
			return Snippet.objects.get(pk=pk)
		except Snippet.DoesNotExist:
			raise Http404


	def get(self, request):
		teams = Team.objects.all()
		team_serializer = TeamSerializer(teams, many = True)
		return Response(team_serializer.data)

	def put(self, request, pk, format=None):
		snippet = self.get_object(pk)
		serializer = TeamSerializer(snippet, data=request.data)
		if serializer.is_valid():
			serializer.save()
			return Response(serializer.data)
		return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)  	

	#def post(self, request):
    #    serializer = TeamSerializer(data=request.data)
    #    if serializer.is_valid():
    #        serializer.save()
    #        return Response(serializer.data, status=status.HTTP_201_CREATED)
    #    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)	
	

def index(request):
    return render(request,'index.html')   

def CountdownTimer(request):
	return render(request, 'CountdownTimer.html')

def table(request):
	return render(request, 'responsive_table.html')

def chart(request):
	#zero=Team.objects.filter(tasks_completed__contains=0)
	#one=Team.objects.filter(tasks_completed__contains=1)
	#two=Team.objects.filter(tasks_completed__contains=2)
	#three=Team.objects.filter(tasks_completed__contains=3)
	#four=Team.objects.filter(tasks_completed__contains=4)
	#five=Team.objects.filter(tasks_completed__contains=4)
	return render(request, 'chartjs.html')

def panel(request):    
    full=Team.objects.all()        
    return render(request, 'panels.html',
              {'full':full})

def table(request):    
    teams=Team.objects.all() 
    tasks=Task.objects.all()       
    return render(request, 'responsive_table.html',
              {'teams':teams,'tasks':tasks})

#def blank(request,team_name):  
#	team = Team.objects.get(team_name= team_name)  
    
           

#	return render(request, 'blank.html', {'team':team})    
def map(request):
	team1=Team.objects.get(team_id=1)
	team2=Team.objects.get(team_id=2)
	team3=Team.objects.get(team_id=3)

	return render(request, 'chartjs.html',{'team1':team1,'team2':team2,'team3':team3})











