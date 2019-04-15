from django.http import HttpResponse
from django.shortcuts import render
from django.views.generic.base import View
#from student.models import loginfo


class Stud(View):

    def get(self,request, *args, **kwargs):
        return render(request, 'login.html')

#     def post(self, request, *args, **kwargs):
#         print("something")
#         hi = loginfo()
#         hi.fname = request.POST.get('First_Name')
#         hi.pwd = request.POST.get('Password')
#         hi.email = request.POST.get('Email_Id')
#         hi.lname = request.POST.get('Last_Name')
#
#         hi.save()
#         return HttpResponse('<h1>Sucessfully Data entered to Database</h1>')
#
#
stud=Stud.as_view()


