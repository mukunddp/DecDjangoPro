from django.shortcuts import render


# Create your views here.
# def contact(request):
#     return HttpResponse('''This is contact HTTP Response''')


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
