from django.urls import path
# from .views import HomeView, PostDetailView, AddPostView, UpdatePostView, DeletePostView
from . import views

urlpatterns = [
    # path("", HomeView.as_view(), name = 'home'), 
    # path("post/<int:pk>", PostDetailView.as_view(), name='post-detail'),
    # path("add_post/", AddPostView.as_view(), name='add-post'),
    # path("post/update/<int:pk>", UpdatePostView.as_view(), name='update-post'),
    # path("post/delete/<int:pk>", DeletePostView.as_view(), name='delete-post')
    path('', views.home, name='home')
]