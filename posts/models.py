from django.db import models
from django.conf import settings

class Post(models.Model):
    POST_TYPES = (
        ('video', 'Video'),
        ('image', 'Image'),
        ('text', 'Text'),
    )

    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='posts')
    post_type = models.CharField(max_length=10, choices=POST_TYPES)
    caption = models.TextField(blank=True, null=True)
    video = models.FileField(upload_to='videos/', blank=True, null=True)
    image = models.ImageField(upload_to='images/', blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.user.username} - {self.post_type}"