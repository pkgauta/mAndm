from django.db import models
from taggit.managers import TaggableManager
from django.contrib.auth.models import User

BLOG_IMAGE_STATUS = (
        ("0", "Hide "),
        ("1", "Publish"),
    )

BLOG_POST_STATUS = (
        ("0", "Draft "),
        ("1", "Publish"),
    )
BLOG_POST_CATEGORY = (
        ("bike", "Bike "),
        ("car", "Car"),
        ("news", "News"),
    )

class BlogImages(models.Model):
    """
        Model for storing the images linked with the post.
    """
    
    post_image = models.ImageField(upload_to='postImages/')
    status = models.CharField(max_length=255, choices=BLOG_IMAGE_STATUS)
    updated_on = models.DateTimeField(auto_now= True)
    created_on = models.DateTimeField(auto_now_add=True)
    
    class Meta:
        ordering = ['-created_on']
    
    
class BlogPost(models.Model):
    """
        Model for storing the post and its details.
    """
    
    title = models.CharField(max_length=200)
    sub_title = models.CharField(max_length=200)
    category = models.CharField(max_length=200, choices=BLOG_POST_CATEGORY)
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='blog_posts')
    content = models.TextField()
    tags = TaggableManager()
    post_image = models.ForeignKey(BlogImages, on_delete=models.CASCADE, related_name='blog_posts')
    status = models.IntegerField(choices=BLOG_POST_STATUS, default=0)
    fb_link = models.CharField(max_length=200, null=True)
    insta_link = models.CharField(max_length=200, null=True)
    tw_link = models.CharField(max_length=200, null=True)
    updated_on = models.DateTimeField(auto_now= True)
    created_on = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-created_on']

    # def __str__(self):
    #     return self.title


# Create your models here.
