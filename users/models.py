from django.db import models


class BlogSettings(models.Model):
    num_pages = models.IntegerField()
