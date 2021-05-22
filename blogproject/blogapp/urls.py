from django.contrib import admin
from django.urls import path
from .views import *

urlpatterns = [
    path('blogdetail/<str:blog_id>', blogdetail, name ="blogdetail"),
    path('blognew/', blognew, name = "blognew"),
    path('blogedit/<str:blog_id>', blogedit, name = "blogedit"),
    path('blogdelete/<str:blog_id>', blogdelete, name = "blogdelete")
]