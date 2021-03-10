from django.db import models
from taggit.managers import TaggableManager
from django.contrib.auth.models import User


class BlogImages(models.Model):
    """
        Model for storing the images linked with the post.
    """
    STATUS = (
        (0, "Hide "),
        (1, "Publish"),
    )
    
    post_image = models.ImageField(upload_to='postImages/')
    status = models.IntegerField(choices=STATUS, default=0)
    updated_on = models.DateTimeField(auto_now= True)
    created_on = models.DateTimeField(auto_now_add=True)
    
    class Meta:
        ordering = ['-created_on']
    
    
class BlogPost(models.Model):
    """
        Model for storing the post and its details.
    """
    STATUS = (
        ("0", "Draft "),
        ("1", "Publish"),
    )
    
    title = models.CharField(max_length=200, unique=True)
    sub_title = models.CharField(max_length=200, unique=True)
    category = models.CharField(max_length=200, unique=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='blog_posts')
    content = models.TextField()
    tags = TaggableManager()
    post_image = models.ForeignKey(BlogImages, on_delete=models.CASCADE, related_name='blog_posts')
    status = models.IntegerField(choices=STATUS, default=0)
    updated_on = models.DateTimeField(auto_now= True)
    created_on = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-created_on']

    def __str__(self):
        return self.title


# Create your models here.
