from django.shortcuts import render
from .models import Settings,Doom,Socialnetworks

# Create your views here.
def index(request):
    settings = Settings.objects.latest("id")
    doom = Doom.objects.latest("id")
    socialnetworks = Socialnetworks.objects.latest("id")
    context ={
        'settings':settings,
        'doom':doom,
        'socialnetworks':socialnetworks,

    }
    return render(request,'index.html',context)