from django.shortcuts import render, get_object_or_404
from 
from django.contrib.auth.models import User
from django.urls import reverse_lazy
from django.contrib.auth.decorators import login_required

# Create your views here.
def index(request):
    return render(request, 'music/index.html')
    
