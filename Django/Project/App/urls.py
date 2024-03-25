# App's own url file
from django.urls import path 
# from .views import first,table,nav,reg,auth,feed,login
from .views import *

 
urlpatterns = [
    # path ('whatever' , function of views file , name = 'whatever you like')
    path('first/', first , name = 'first'),
    path('table/', table , name='tb'),
    path('nav/', nav, name='nav'),
    path('auth/', auth, name='auth'),
    path('reg/' , reg, name='reg'),
    path('feed/' , feed, name='feed'),
    path('login/' , login, name='login'),

]