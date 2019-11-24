from django.shortcuts import render
from django.http import HttpResponse
from App.models import Student
# Create your views here.
def hello(request):
    return HttpResponse("hello world!")

def my(request):
    return HttpResponse("你是一个天才！")

def index(request):
    return render(request,"index.html")

def home(request):
    return render(request,"home.html")

def addStudent(request):   
    for i in range(5):
        student = Student()
        student.s_name = 'ee'+ str(i)
        student.s_age = 18 + i
        student.save()
    return HttpResponse('添加成功！'+ student.s_name)

def getStudent(request):
    students = Student.objects.all()
    for i in students:
        print(i.s_name)
    studir = {
       "stu":students 
    }
    return render(request,"studentList.html",context=studir)
