from django.urls import path

from . import views

urlpatterns = [
    path('', views.index),
    path('description/', views.description),
    path('abilities/',views.abilities),
    path('education/',views.education),
    path('projects/',views.education),
    path('contact/',views.contact),
]
