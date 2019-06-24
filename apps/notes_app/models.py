from django.db import models
# from ..login_app.models import User

class Note(models.Model):
    title = models.CharField(max_length=255)
    category = models.CharField(max_length=255)
    form_type = models.CharField(max_length=255)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
