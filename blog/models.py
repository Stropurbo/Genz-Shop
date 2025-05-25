from django.db import models
from cloudinary.models import CloudinaryField

class BlogModel(models.Model):
    name = models.CharField(max_length=200)
    description = models.TextField()
    image = CloudinaryField('image')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name
    