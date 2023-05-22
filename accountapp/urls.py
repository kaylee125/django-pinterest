
from django.urls import path

from accountapp.views import helloworld

#브라우저에서 
app_name='accountapp'

urlpatterns=[
    #path(route,view,name=)
    path('helloworld/',helloworld,name='helloworld')
]