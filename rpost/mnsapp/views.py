from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def index(request):
    context = {}
    return render(request, 'index.html', context)

def blog(request):
    context = {}
    return render(request, 'dashboard.html', context)
def blog2(request):
    context = {}
    return render(request, 'new.html', context)