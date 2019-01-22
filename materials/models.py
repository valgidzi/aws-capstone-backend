from django.db import models

# Create your models here.

class Handout(models.Model):
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    text = models.TextField()
    words = models.TextField()
    definitions = models.TextField()
    user = models.TextField()
    score = models.TextField()
    title = models.TextField()
    directions = models.TextField(default=' ')
    display_words = models.BooleanField(default=True)
    display_definitions = models.BooleanField(default=True)
    column_order = models.TextField(default=' ')
