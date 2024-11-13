from django.shortcuts import render



# Create your views here.
def index(request):

    return render(request,'bio/info.html')

def description(request):
    return render(request,'bio/description.html' )

def abilities(request):
    return render(request,'bio/abilities.html' )

def education(request):
    return render(request,'bio/education.html' )

def projects(request):
    return render(request,'bio/projects.html' )

def contact(request):
    return render(request,'bio/contact.html' )




