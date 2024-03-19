from django.db import models
from django.contrib.auth.models import User

# # Create your models here.

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE) # associate one user to one profile
    follows = models.ManyToManyField(
        'self', # relationship between same model
        related_name='followed_by', # 
        symmetrical=False, # other user does not have to follow back (one way)
        blank=True # do not have to follow anybody
        )
    
    def __str__(self) -> str:
        return f"{self.user.username}'s Profile"

# class Post(models.Model):
#     title = models.CharField(max_length=255)
#     title_tag = models.CharField(max_length=255)
#     author = models.ForeignKey(User, on_delete=models.CASCADE)
#     body = models.TextField()

#     def __str__(self) -> str:
#         return self.title + ' | ' + str(self.author)
    
#     def get_absolute_url(self):
#         from django.urls import reverse
#         # return reverse('post-detail', kwargs={"pk": self.pk}) # redirect user to newly made individual entry
#         return reverse('home') # redirect them back to the home page