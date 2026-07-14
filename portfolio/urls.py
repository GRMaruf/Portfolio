from django.urls import path
from portfolio.views import *

urlpatterns = [
    path('current_user/dashboard', dashboard, name='dashboard'),
    
    path('', profile, name='profile'),
    path('<str:username>', profile, name='profile'),
    path('<str:username>/contact', contact, name='contact'),
    path('<str:username>/projects', projects, name='projects'),
    path('<str:username>/resume', resume, name='resume'),
]
