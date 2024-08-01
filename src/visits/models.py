from django.db import models

from django.contrib.auth.models import User

# Create your models here.

class PageVisit(models.Model):
    """
    Track visits to a certain page of your application.
    """
    # user = models.ForeignKey()
    path = models.TextField(null=True, blank=True)
    timestamp = models.DateTimeField(auto_now_add=True)
