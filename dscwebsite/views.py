from django.shortcuts import render
from .models import events, hof, team, services

# Create your views here.
def index(request):
    servs = services.objects.all()
    eves = events.objects.all()
    hofs = hof.objects.all()
    teams = team.objects.all()

    return render(request,"index.html", {'eves':eves ,
                                         'hofs':hofs,
                                         'teams':teams,
                                         'servs':servs })