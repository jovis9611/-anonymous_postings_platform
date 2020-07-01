from django.db import models
from django.shortcuts import reverse

# Create your models here.
class Post(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField(blank=True)
    photo = models.URLField(blank=True)
    # location = models.CharField(max_length=100)
 
    created_at = models.DateTimeField(auto_now_add=True)
    
    # return title to admin panel
    def __str__(self):
        return self.title
    
    
    def get_absolute_url(self):
        return reverse("trips:post_detail", kwargs={
            'pk': self.pk
        })

