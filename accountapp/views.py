from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
def helloword(request):
    return HttpResponse('helloworld')