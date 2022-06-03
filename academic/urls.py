from django.urls import path
from . import views

urlpatterns = [

    path('', views.home),
    path('registerCourse/', views.registerCourse),
    path('deleteCourse/<id>', views.deleteCourse)
]
    