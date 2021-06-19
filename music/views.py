from .models import Music
from django.shortcuts import render, get_object_or_404

from django.contrib.auth.models import User
from django.urls import reverse_lazy
from django.contrib.auth.decorators import login_required

# Create your views here.
def index(request):
    return render(request, 'music/index.html')

def music(request):
    song_list = Music.objects.all()
    return render(request, 'music/music.html', {'song_list': song_list})

    
