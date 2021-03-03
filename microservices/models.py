from django.db import models
from django.contrib.auth.models import User

class UserProfile(models.Model):
    """
        Model to extend the user information
    """
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    bio = models.TextField()
    fb_profile_url = models.CharField(max_length=255)
    insta_profile_url = models.CharField(max_length=255)
    yt_profile_url = models.CharField(max_length=255)
    tw_profile_url = models.CharField(max_length=255)
    hobbies = models.CharField(max_length=255)
    avatar = models.ImageField(upload_to ='profilePics/')
    updated_on = models.DateTimeField(auto_now= True)
    created_on = models.DateTimeField(auto_now_add=True)
    
    def get_full_name(self):
        '''
        Returns the first_name plus the last_name, with a space in between.
        '''
        full_name = '%s %s' % (self.user.first_name, self.user.last_name)
        return full_name.strip()

    def get_short_name(self):
        '''
        Returns the short name for the user.
        '''
        return self.user.first_name

    def email_user(self, subject, message, from_email=None, **kwargs):
        '''
        Sends an email to this User.
        '''
        send_mail(subject, message, from_email, [self.user.email], **kwargs)
# Create your models here.
