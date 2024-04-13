from django.shortcuts import render,redirect
# Create your views here.
from .models import StudentsData
def index(request):
    students=StudentsData.objects.all()
    return render(request,'index.html', {'students':students})
def add_student(request):
    if request.method=="GET":
        return render(request,'add_student.html')
    else:
        StudentsData(
        score=request.POST.get('scour')
        ).save()
        return redirect('index')
def update_student(request,id):
    student=StudentsData.objects.get(id=id)
    if request.method=="GET":
        return render(request,'update_student.html',{'student':student})
    else:
        student.first_name=request.POST.get('fname')
        student.last_name=request.POST.get('lname')
        student.course=request.POST.get('course')
        student.fee=request.POST.get('fee')
        student.assignment1=request.POST.get('a1')
        student.assignment2=request.POST.get('a2')
        student.assignment3=request.POST.get('a3')
        student.assignment4=request.POST.get('a4')
        student.institute=request.POST.get('institute')
        student.location=request.POST.get('location')
        student.save()
        return redirect('index')

def delete_student(request,id):
    student=StudentsData.objects.get(id=id)
    student.delete()
    return redirect('index')
