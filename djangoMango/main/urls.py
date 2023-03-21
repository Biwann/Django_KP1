from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name = 'home'),
    path('about-us', views.about, name = 'about'),
    path('check', views.check, name = 'check'),
    path('checkid', views.checkid, name = 'checkid'),
    path('generate', views.indexGen, name = 'Gen'),
]
