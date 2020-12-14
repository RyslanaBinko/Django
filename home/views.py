from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.


def home(request):
    request.GET

    request.POST
    return render(request, "index.html")
