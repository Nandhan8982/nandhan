from django.urls import path
from . import views

urlpatterns = [
                path('', views.blog2, name='home'),
                path('blog', views.blog, name='blog'),
                path('home', views.index, name='home'),



    ]