from django.shortcuts import render, redirect
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from .models import Profile, Idea
from .forms import IdeaForm
from django.urls import reverse_lazy
from django.http import JsonResponse
from django.contrib import messages

# Create your views here.

def home(request):
    if request.user.is_authenticated:
        form = IdeaForm(request.POST or None)
        if request.method == 'POST':
            if form.is_valid():
                idea = form.save(commit=False)
                idea.user = request.user
                idea.save()
                messages.success(request, ('Your idea has been successfully submitted'))
                return redirect('home')
        ideas = Idea.objects.all().order_by('-created_at')
        return render(request, 'feed/home.html', {'ideas':ideas, 'form':form})
    else:
        ideas = Idea.objects.all().order_by('-created_at')
        return render(request, 'feed/home.html', {'ideas':ideas})


def profile_list(request):
    if request.user.is_authenticated:
        profiles = Profile.objects.exclude(user=request.user) # query all users except self
        return render(request, 'feed/profile_list.html', {'profiles': profiles})
    else:
        messages.success(request, ('Login to view this page'))
        return redirect('home')
    

def profile(request, pk):
    if request.user.is_authenticated:
        profile = Profile.objects.get(user_id=pk)
        ideas = Idea.objects.filter(user_id=pk).order_by('-created_at')
        # post form logic for follow/unfollow
        if request.method == 'POST':
            # get current user id
            current_user_profile = request.user.profile
            # get form data
            action = request.POST['follow']
            # decide to follow or unfollow
            if action == 'unfollow':
                current_user_profile.follows.remove(profile)
            elif action == 'follow':
                current_user_profile.follows.add(profile)
            # save profile
            current_user_profile.save()

        return render(request, 'feed/profile.html', {'profile': profile, 'ideas': ideas})
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