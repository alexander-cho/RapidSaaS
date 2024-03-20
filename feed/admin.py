from django.contrib import admin
from .models import Profile, Idea#, Post
from django.contrib.auth.models import Group, User

# Register your models here.
admin.site.unregister(Group)
# admin.site.register(Post)

# Mix profile info into user info
class ProfileInline(admin.StackedInline):
    model = Profile
    fields = []

# Extend User Model
class UserAdmin(admin.ModelAdmin):
    model = User
    # Just display username fields on model page
    fields = ['username']
    inlines = [ProfileInline]

# Unregister initial user
admin.site.unregister(User)
# re-register
admin.site.register(User, UserAdmin)

# admin.site.register(Profile)

admin.site.register(Idea)
