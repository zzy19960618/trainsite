from django.views.generic import TemplateView
from django.views.generic import CreateView
from django.views.generic import UpdateView
from django.shortcuts import render
from django.http import HttpResponse

from django.views.generic import ListView
from .models import Post


def test(request):
    return render(request, 'test.html')


def homepageview(request):
    return render(request, 'about.html')


class BlogHomeView(ListView):
    model = Post
    template_name = 'blog_home.html'


class AboutPageView(TemplateView):
    template_name = 'about.html'


class BlogCreateView(CreateView):
    model = Post
    template_name = 'blog_create.html'
    fields = '__all__'

class BlogUpdateView(UpdateView):
    model = Post
    fields = ['title', 'text']
    template_name = 'blog_update.html'