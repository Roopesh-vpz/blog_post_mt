from django.urls import path
from .views import *

urlpatterns = [
    path('index/', index,name='home'),
    path('login/', login,name='login'),
    path('home/', homepage,name='home'),
    path('logout/', logout,name='logout')
    
]