from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
def helloworld(request):
    #HttpResponse:view에서 응답을 직접 만들어서 웹으로 넘겨주는 방식
    #render:templates애 있는 Html파일에 값이 들어갈 수 있도록 하는 기능
    return render(request,'accountapp/helloworld.html')