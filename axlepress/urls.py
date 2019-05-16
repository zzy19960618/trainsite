from django.urls import path
from . import views

urlpatterns = [
    #path('base', views.base),
    path('', views.home, name='home'),
    path('about', views.about, name='about'),

    path('main', views.index, name='main'),
    path('refresh', views.getData),

    path('inquiry', views.inquiry),

    path('config', views.cfgtrain, name='config'),
#    path('config', views.configTrain),
    #path('trainsite', ),
]
