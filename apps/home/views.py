from django.shortcuts import render
from .models import Settings,Doom

# Create your views here.
def index(request):
    settings = Settings.objects.latest("id")
    doom = Doom.objects.latest("id")
    context ={
        'settings':settings,
        'doom':doom,

    }
    return render(request,'index.html',context)