from django.shortcuts import render
from django.views.generic import ListView, DetailView
from .models import Post

# Create your views here.

# def home(request):
#     return render(request, 'feed/home.html', {})

class HomeView(ListView):
    model = Post
    template_name = 'feed/home.html'


class PostDetailView(DetailView):
    model = Post
    template_name = 'feed/post_detail.html'