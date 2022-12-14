# from django.conf.urls import patterns, url
from .views import *
from django.urls import path,include
from .views import UserSignin, UserLogin,ActivateAccount
from django.contrib.auth.views import LogoutView

app_name='bususer'

urlpatterns=[
    path('signup/', UserSignin.as_view(), name='signup'),
    path('', UserLogin.as_view(), name='login'),
    path("logout/", LogoutView.as_view(), name="logout"),
    path('activate/<str:uidb64>/<str:token>',ActivateAccount.as_view(),name='activate'),
    path('sent/', activation_sent_view, name='sent'),
    path('invalid',activation_invalid_view, name='invalid'),

  



  
]