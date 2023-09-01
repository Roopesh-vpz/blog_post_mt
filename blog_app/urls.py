

from django.urls import include, path
# import routers
from rest_framework import routers

# import everything from views
from .views import *
  
# define the router
router = routers.DefaultRouter()

router.register('post',PostView)
urlpatterns = [
    path('api/', include(router.urls)),
    
]