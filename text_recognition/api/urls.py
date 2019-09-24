from django.urls import path,include
from . import views
from rest_framework import routers

router = routers.DefaultRouter()
router.register('aadhar', views.AadharView)

urlpatterns = [
    #path('admin/', admin.site.urls),
    #path('',include('api.urls')),
    path('recog',views.recog, name= 'recog'),

    path('',include(router.urls))
]