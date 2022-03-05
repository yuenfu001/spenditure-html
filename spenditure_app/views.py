from django.shortcuts import render

# Create your views here.
def mainpage(request):
    context = {}
    return render(request,'index.html' ,context)

def homepage(request):
    context = {}
    return render(request,'home.html' ,context)

def services(request):
    context = {}
    return render(request,'services.html', context)

def about(request):
    context = {}
    return render(request,'about.html', context)

# def home(request):
#     context = {}
#     return render(request, context)

# def home(request):
#     context = {}
#     return render(request, context)
