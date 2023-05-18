
from django.urls import path

from pinterest.accountapp.views import helloword

#브라우저에서 
app_name='accountapp'

urlpatterns=[
    #path(route,view,name=)
    path('helloworld/',helloword,name='helloworld')
]