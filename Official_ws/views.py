from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request,'Official_ws/index.html')


def about_us(request):
    return render(request, 'Official_ws/about_us.html')


def courses(request):
    return render(request,'Official_ws/courses.html')


def login(request):
    return render(request,'Official_ws/login.html')