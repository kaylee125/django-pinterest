from django.http import HttpResponse,HttpResponseRedirect
from django.contrib.auth.models import User
from django.shortcuts import render
from django.urls import reverse, reverse_lazy
from accountapp.models import Helloworld
from django.views.generic import CreateView
from django.contrib.auth.forms import UserCreationForm

# Create your views here.
def helloworld(request):
    #HttpResponse:view에서 응답을 직접 만들어서 웹으로 넘겨주는 방식
    #render:templates애 있는 Html파일에 값이 들어갈 수 있도록 하는 기능
    # return render(request,'accountapp/helloworld.html')

    if request.method=="POST":
        temp=request.POST.get('helloworld_input') #request>POST>name이 helloworld_input인 데이터를 가져오라는 명령어
        
        #모델 객체 생성 및 데이터 DB저장
        new_Helloworld=Helloworld()
        new_Helloworld.text=temp
        new_Helloworld.save()

        #모든 데이터 다 가져오기
        helloworld_list=Helloworld.objects.all()

        # return render(request,'accountapp/helloworld.html',context={'helloworld_list':helloworld_list})
        return HttpResponseRedirect(reverse('accountapp:helloworld'))
    else:
        # helloworld_list=Helloworld.objects.all()
        return render(request,'accountapp/helloworld.html',context={'helloworld_list':helloworld_list})

class AccountCreateView(CreateView):
    model=User
    form_class= UserCreationForm
    #계정생성에 성공했을 경우 어느 경로로 다시 연결할건지 설정
    success_url=reverse_lazy('accountapp:helloworld')
    #회원가입 화면 html 지정
    template_name='accountapp/create.html'

