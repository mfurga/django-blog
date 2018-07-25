from django.db import models


class Contact(models.Model):
    email = models.EmailField()
    message = models.TextField()
    date = models.DateTimeField()

    class Meta:
        ordering = ['-date']

    def __str__(self):
        return self.email
