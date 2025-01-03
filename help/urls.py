from django.urls import path
from django.conf.urls import handler404
from . import views
handler404 = views.custom_404
urlpatterns = [
    path('', views.index, name='index'),
    path('about', views.about, name='about'),
    path('terms', views.terms, name='terms'), 
    path('privacy', views.privacy, name='privacy'), 
    path('requestinfo', views.requestinfo, name='requestinfo'), 
    path('register', views.register, name='register'), 
    path('vs', views.vs, name='vs'),
    path('gmail', views.gmail, name='gmail'), 
    path('success', views.success, name='success'),
    path('successvs', views.successvs, name='successvs'), 
    path('successreg', views.successreg, name='successreg'), 

    
]

