from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from django.contrib.auth import get_user_model


User = get_user_model()


# Create your views here

@login_required
def profile_view(request, username=None, *args, **kwargs):
    print(request)
    user = request.user
    profile_user_obj = get_object_or_404(User, username=username)
    is_me = profile_user_obj == user
    return HttpResponse(f"Hello there, {profile_user_obj.username}, you are user number {profile_user_obj.id}. User of this profile is the same as the user of the current request: {is_me}")
