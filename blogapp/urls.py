from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name="index"),
    path('oldposts/', views.moreindex, name="moreindex"),
    path('contact/', views.contact, name="contact"),
    path('contactsubmit/', views.submitcontact, name="submitcontact"),
    path('display/<slug>', views.display, name="display")
]
