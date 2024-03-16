from django.shortcuts import render
from django.views.generic import ListView, DetailView, CreateView
from .models import Post
from .forms import PostForm

# Create your views here.

# def home(request):
#     return render(request, 'feed/home.html', {})

class HomeView(ListView):
    model = Post
    template_name = 'feed/home.html'


class PostDetailView(DetailView):
    model = Post
    template_name = 'feed/post_detail.html'


class AddPostView(CreateView):
    model = Post
    form_class = PostForm
    template_name = 'feed/add_post.html'
    # fields = ['title', 'body']
    # fields = '__all__'