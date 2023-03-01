from django.db import models
from django.conf import settings
from django.contrib.auth.models import User

class BlogEntryModel(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, null=True, blank=True)
    body = models.CharField(max_length=5000)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return (
            f"{self.user} "
            f"({self.created_at:%Y-%m-%d %H:%M}): "
            f"{self.body[:30]}..."
        )