from django.db import models

class PostsManager(models.Manager):
    def get_recent_data(self, count=5):
        return super(PostsManager, self).all().order_by('-created_at')[:count]

class Posts(models.Model):
    name = models.CharField(max_length=30)
    description = models.TextField()
    url = models.TextField()
    created_at = models.DateTimeField()

    objects = PostsManager()
