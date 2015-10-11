from django.db import models

class Posts(models.Model):
    name = models.CharField(max_length=30)
    description = models.TextField()
    url = models.TextField()
    created_at = models.DateTimeField()
