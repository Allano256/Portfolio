from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='home'),
    path('education/',views.education, name='education'),
    path('projects/',views.projects,name='projects'),
    
]
