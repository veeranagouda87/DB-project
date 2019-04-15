from django.contrib import admin
from django.urls import include, path
from student.views import stud

urlpatterns = [

    path('hi/',  view=stud, name='stud')
]
