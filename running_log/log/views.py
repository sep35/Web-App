from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
from .models import Users

def index(request):
    output = ', '.join([p.name for p in Users.objects.all()])
    return HttpResponse(output)
