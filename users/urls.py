from django.contrib import admin
from django.urls import path , include
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('register/', views.register, name='register'),
    path('login/', views.login_user, name='login'),
    path('logout/',views.logout_user,name='logout'),
    path('upload/', views.upload_resource, name='upload'),
    path('resources/', views.resource_list, name='resources'),
    path('contacts/',views.contacts,name ='contacts'),
    path('about/',views.about,name='about'),
    path('resource/<int:resource_id>/', views.view_resource, name='view_resource'),
]
