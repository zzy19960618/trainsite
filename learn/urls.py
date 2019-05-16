from django.urls import path
from learn import views


urlpatterns = [
    path('', views.homepageview),
    path('test', views.test),

    path('test/home', views.BlogHomeView.as_view(), name='learnhome'),
    path('test/about', views.AboutPageView.as_view(), name='learnabout'),
    path('test/updateBlog/<int:pk>', views.BlogUpdateView.as_view(), name='updateBlog'),
    path('test/createBlog', views.BlogCreateView.as_view(), name='createBlog'),
]