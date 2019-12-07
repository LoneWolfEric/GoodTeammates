from django.contrib import admin
from django.urls import path, re_path, include
from login.views import index,login,logout


urlpatterns = [
    path('login/', login),
    path('logout/', logout),
    path('index/', index),
    path('', index),
    # re_path('(.*?)', index),
]
