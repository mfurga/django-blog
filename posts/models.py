from django.conf import settings
from django.db import models


class Post(models.Model):
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    title = models.CharField(max_length=50)
    content = models.TextField()
    tags = models.CharField(max_length=50)
    publish = models.DateTimeField()
    active = models.BooleanField(default=True)

    slug = models.SlugField(unique=True, blank=True, null=True)

    class Meta:
        ordering = ['-publish']

    def __str__(self):
        return self.title
