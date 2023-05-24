
from django.urls import path

from accountapp.views import helloworld
from accountapp.views import AccountCreateView

#브라우저에서 
app_name='accountapp'

urlpatterns=[
    #path(route,view,name=)
    path('helloworld/',helloworld,name='helloworld'),
    path('create/',AccountCreateView.as_view(),name='create'),
]