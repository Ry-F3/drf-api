from django.db import models

# Create your models here.
from django.contrib.auth.models import User

class Profile(models.Model):
    owener = models.OneToOneField(User, on_delete=models.CASCADE)
    created_at = models.dateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    name = models.CharField(max_length=255, blank=True)
    content = models.TextField(blank=True)
    image = models.ImageField(
        upload_to='images/', default='../default_post_gxkdet'
    )
    
    class Meta:
        ordering = ['-created_at']
        
    def __str__(self):
        return f"{self.owner}'s profile"
    
post_save.connect(create_profile, sender=User)