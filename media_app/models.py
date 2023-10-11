from django.db import models
from django.contrib.auth import get_user_model

# User
User = get_user_model()

# Profile
class Profile(models.Model):
    user = models.ForeignKey(User, related_name='profile', on_delete=models.CASCADE)
    description = models.TextField(blank=True, null=True)
    image = models.ImageField(blank=True, null=True, upload_to='profile_images')
    location = models.CharField(max_length=100, blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    class Meta:
        db_table = "profile"
    
# Post
class Post(models.Model):
    user = models.ForeignKey(User, related_name='post', on_delete=models.CASCADE)
    caption = models.TextField()
    image = models.ImageField(blank=True, null=True, upload_to='post_images')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    class Meta:
        db_table = "post"
    
# LikePost
class LikePost(models.Model):
    post = models.ForeignKey(Post, related_name='like_post', on_delete=models.CASCADE)
    # here we are storing the user who made the like
    user = models.ForeignKey(User, related_name='like_post', on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:        
        db_table = "like_post"
    

    