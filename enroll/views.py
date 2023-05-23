from django.shortcuts import render
from django.http import JsonResponse

from .forms import StudentRegistration
from .models import User


def home(request):
    form = StudentRegistration()
    stud = User.objects.all()
    return render(request, 'enroll/home.html', {'form': form, 'stud': stud})

def saveData(request):
    if request.method == 'POST':
        form = StudentRegistration(request.POST)
        if form.is_valid():
            sid = request.POST.get('stuid')
            name = request.POST['name']
            email = request.POST['email']
            password = request.POST['password']
            if sid == '':   # if it is a new user
                usr = User(name=name, email=email, password=password)
            else:           # if it is a existing user (edit)
                usr = User(id=sid, name=name, email=email, password=password)
            usr.save()
            stud = User.objects.values()
            student_data = list(stud)
            return JsonResponse({'status': 'Save', 'student_data': student_data})
        else:
            return JsonResponse({'status': 0})
        

def deleteData(request):
    if request.method == 'POST':
        id = request.POST.get('sid')
        pi = User.objects.get(pk=id)
        pi.delete()
        return JsonResponse({'status': 1})
    else:
        return JsonResponse({'status': 0})


def editData(request):
    if request.method == 'POST':
        id = request.POST.get('sid')
        student = User.objects.get(pk=id)
        student_data = {"id": student.id, 'name': student.name, 'email': student.email, 'password': student.password}
        return JsonResponse(student_data)