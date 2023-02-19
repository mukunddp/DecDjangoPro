from django.http import HttpResponse
from django.shortcuts import render


# Create your views here.
def contact(request):
    return HttpResponse('''This is contact HTTP Response''')


def home(request):
    return render(request, 'index.html')


def about(request):
    return render(request, 'about.html')
