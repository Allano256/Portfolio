from django.shortcuts import render



# Create your views here.
def index(request):

    return render(request,'bio/index.html')

def education(request):
    return render(request,'bio/education.html' )

def projects(request):
    return render(request,'bio/projects.html' )






