import imp
from sqlite3 import Cursor
from django.shortcuts import redirect, render
from .models import Grade

# Create your views here.

def home(request):
    coursesListed = Grade.objects.all()
    return render(request, "courseManagement.html", {"grades":coursesListed})

def registerCourse(request):
    id = request.POST['txtId']
    name = request.POST['txtName']
    credits = request.POST['txtCredits']

    grade = Grade.objects.create(id=id, name=name, credits=credits) 
    return redirect('/')