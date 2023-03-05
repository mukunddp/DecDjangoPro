from django.shortcuts import render, redirect
from .models import Student

# Create your views here.
# def contact(request):
#     return HttpResponse('''This is contact HTTP Response''')

# CRUD
# Create a Entry in DB
# Read the Entries from DB
# Update the Entries from DB
# Delete the Entries from DB
def store_student(request):
    s = Student()
    s.name_student = request.POST.get('student_name')
    s.name_college = request.POST.get('clg_name')
    s.department = request.POST.get('department')
    s.year_pass = request.POST.get('year')
    s.mobile = request.POST.get('mobile')
    s.save()
    return redirect('index')

def add_student(request):
    return render(request, 'add_student.html')

def home(request):
    return render(request, 'index.html')


def posts(request):
    return render(request, 'post.html')


def jobs(request):
    return render(request, 'jobs.html')


def login(request):
    return render(request, 'login.html')


def register(request):
    return render(request, 'register.html')


def profile(request):
    return render(request, 'profile.html')


def about(request):
    return render(request, 'about.html')
