from django.shortcuts import render

# Create your views here.

from django.http import HttpResponse
from hunt_app.models import Team,Task
from django.template import RequestContext
from django.shortcuts import render_to_response
from django.http import HttpResponseRedirect, HttpResponse
from django.shortcuts import get_object_or_404, render





def index(request):
    return render(request,'index.html')   


def panel(request):    
    full=Team.objects.all()        
    return render(request, 'panels.html',
              {'full':full})



