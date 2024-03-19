from django.shortcuts import render
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
# from .models import Post
# from .forms import PostForm
from django.urls import reverse_lazy
from django.http import JsonResponse

# Create your views here.

def home(request):
    return render(request, 'feed/home.html', {})


# class HomeView(ListView):
#     model = Post
#     template_name = 'feed/home.html'
#     ordering = ['-id'] # ideally by date, not in model yet


# class PostDetailView(DetailView):
#     model = Post
#     template_name = 'feed/post_detail.html'


# class AddPostView(CreateView):
#     model = Post
#     form_class = PostForm
#     template_name = 'feed/add_post.html'
#     # fields = ['title', 'body']
#     # fields = '__all__'


# class UpdatePostView(UpdateView):
#     model = Post
#     template_name = 'feed/update_post.html'
#     fields = ['title', 'title_tag', 'body']


# class DeletePostView(DeleteView):
#     model = Post
#     template_name = 'feed/delete_post.html'
#     success_url = reverse_lazy('home')