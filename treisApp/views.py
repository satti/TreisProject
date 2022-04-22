from unicodedata import name
from django.http import HttpResponse
from django.shortcuts import render
from treisApp.models import Student
# Create your views here.
from treisApp.models import Student
def student_create(request):
    if request.method == 'POST':
        rno = request.POST.get("rollno")
        sname = request.POST.get("name")
        addr = request.POST.get("address")
        student = Student(rollno=rno,name=sname,address=addr)
        student.save()
        return HttpResponse("Data inserted Successfully")
    else:
        return render(request,'studentcreation.html')