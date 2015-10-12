from django.db import models

class Posts(models.Model):
    name = models.CharField(max_length=30)
    description = models.TextField()
    url = models.TextField()
    created_at = models.DateTimeField()

    def get_recent_data(count=5):
        return self.objects.all().order_by('-created_at')[:count]
