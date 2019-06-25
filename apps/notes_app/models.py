from django.db import models
from ..login_app.models import User

class Note(models.Model):
    title = models.CharField(max_length=255)
    category = models.CharField(max_length=255)
    form = models.CharField(max_length=255)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

class Category(models.Model):
    name = models.CharField(max_length=255)
    child = models.ManyToManyField(Note, related_name="categories")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    