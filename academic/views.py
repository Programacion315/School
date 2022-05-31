import imp
from sqlite3 import Cursor
from django.shortcuts import render
from .models import Grade

# Create your views here.

def home(request):
    coursesListed = Grade.objects.all()
    return render(request, "courseManagement.html", {"grades":coursesListed})
