from django.shortcuts import render, redirect
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from .models import Profile#,Post
# from .forms import PostForm
from django.urls import reverse_lazy
from django.http import JsonResponse
from django.contrib import messages

# Create your views here.

def home(request):
    return render(request, 'feed/home.html', {})


def profile_list(request):
    if request.user.is_authenticated:
        profiles = Profile.objects.exclude(user=request.user) # query all users except self
        return render(request, 'feed/profile_list.html', {'profiles': profiles})
    else:
        messages.success(request, ('Login to view this page'))
        return redirect('home')

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